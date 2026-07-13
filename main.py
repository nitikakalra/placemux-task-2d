import pandas as pd
import ast
import re

from src.explainability import generate_explanation
from src.shortlisting import shortlist_candidates
from src.metrics import evaluate_model
from src.save_results import save_json


def extract_skills(text):

    if pd.isna(text):
        return []

    text = str(text).lower()

    skills_list = [

        "python",
        "java",
        "javascript",
        "react",
        "html",
        "css",
        "sql",
        "mongodb",
        "git",
        "aws",
        "communication",
        "leadership",
        "project management",
        "data analysis",
        "machine learning",
        "docker",
        "cloud",
        "c++"

    ]

    found = []

    for skill in skills_list:

        if skill in text:
            found.append(skill)

    return list(set(found))


def calculate_match(candidate_text, job_text):

    candidate_skills = extract_skills(candidate_text)

    job_skills = extract_skills(job_text)


    matched = list(
        set(candidate_skills)
        &
        set(job_skills)
    )


    missing = list(
        set(job_skills)
        -
        set(candidate_skills)
    )


    if len(job_skills) > 0:

        score = round(
            (len(matched) / len(job_skills)) * 100,
            2
        )

    else:

        score = 0


    return {

        "candidate_skills":
        candidate_skills,

        "job_skills":
        job_skills,

        "matched_skills":
        matched,

        "missing_skills":
        missing,

        "baseline_score":
        score,

        "match_score":
        score

    }



jobs = pd.read_csv("data/jobs.csv")

resumes = pd.read_csv("data/resumes.csv")


print("Jobs:", len(jobs))
print("Resumes:", len(resumes))


selected_job = jobs.sample(1).iloc[0]

candidate = resumes.sample(1).iloc[0]


print("\nSelected Job:")
print(selected_job["job_title"])


candidate_text = candidate["Resume_str"]


job_text = (

    str(selected_job["job_title"])

    +

    str(selected_job["job_description"])

    +

    str(selected_job["job_skill_set"])

)



result = calculate_match(
    candidate_text,
    job_text
)



print("\nCandidate Skills:")
print(result["candidate_skills"])


print("\nJob Skills:")
print(result["job_skills"])


print("\nMatched Skills:")
print(result["matched_skills"])


print("\nMissing Skills:")
print(result["missing_skills"])


print("\nBaseline Skill Overlap Score:")
print(result["baseline_score"])



metrics = evaluate_model(
    resumes,
    jobs
)


print("\nMODEL METRICS")
print(metrics)



explanation = generate_explanation(

    int(candidate["ID"]),

    int(selected_job["job_id"]),

    result["match_score"],

    result["matched_skills"],

    result["missing_skills"]

)



final_result = {


    "candidate_id":
    int(candidate["ID"]),


    "job_id":
    int(selected_job["job_id"]),


    "match_score":
    result["match_score"],


    "explanation":
    explanation

}



print("\nFINAL EXPLANATION")
print(final_result)



shortlisted_candidates = shortlist_candidates(

    resumes,

    selected_job

)



print("\nTOP 5 SHORTLISTED CANDIDATES")

for candidate_result in shortlisted_candidates:

    print(candidate_result)



if len(result["matched_skills"]) == 0:

    edge_response = {

        "status":
        "Rejected",

        "reason":
        "No required skills matched."

    }

else:

    edge_response = {

        "status":
        "Processed",

        "reason":
        "Candidate has skill alignment."

    }



print("\nEDGE CASE TEST")
print(edge_response)



save_json(
    final_result,
    "explanation_result.json"
)


save_json(
    shortlisted_candidates,
    "shortlist.json"
)


save_json(
    metrics,
    "metrics.json"
)



experiment_log = {


    "task":
    "Phase 2 Task 4 - Match Explainability",


    "dataset":

    {

        "jobs":
        len(jobs),

        "resumes":
        len(resumes)

    },


    "baseline_score":
    result["baseline_score"],


    "metrics":
    metrics,


    "explainability":

    [

        "matched_skills",

        "missing_skills",

        "match_score",

        "recommendation"

    ]

}



save_json(

    experiment_log,

    "experiments/experiment_log.json"

)