def extract_skills(text):

    skills = [

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
        "cloud"

    ]

    text = str(text).lower()

    found = []

    for skill in skills:

        if skill in text:
            found.append(skill)

    return list(set(found))


def shortlist_candidates(resumes, job):


    job_text = (

        str(job["job_title"])

        +

        str(job["job_description"])

        +

        str(job["job_skill_set"])

    )


    job_skills = extract_skills(job_text)


    results = []


    for _, resume in resumes.iterrows():


        resume_text = resume["Resume_str"]


        candidate_skills = extract_skills(resume_text)


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



        results.append(

            {

                "candidate_id":

                int(resume["ID"]),


                "match_score":

                score,


                "matched_skills":

                matched,


                "missing_skills":

                missing

            }

        )


    results = sorted(

        results,

        key=lambda x:x["match_score"],

        reverse=True

    )


    return results[:5]