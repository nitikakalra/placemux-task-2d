def skill_overlap_score(
        candidate_skills,
        job_skills
):


    if len(job_skills)==0:
        return 0



    matched = set(candidate_skills).intersection(
        set(job_skills)
    )


    score = (
        len(matched)
        /
        len(job_skills)
    ) * 100



    return round(score,2)