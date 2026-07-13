def generate_explanation(
    candidate_id,
    job_id,
    match_score,
    matched_skills,
    missing_skills
):


    if match_score >= 70:

        recommendation = (
            "Strong Match. Candidate is suitable for shortlisting."
        )

        status = "Shortlisted"

        reason = (
            "Candidate meets required skill alignment."
        )


    elif match_score >= 40:

        recommendation = (
            "Moderate Match. Candidate should be reviewed."
        )

        status = "Review Required"

        reason = (
            "Candidate has partial skill alignment and should be reviewed."
        )


    else:

        recommendation = (
            "Low Match. Skill alignment is limited."
        )

        status = "Rejected"

        reason = (
            "Candidate does not meet minimum skill threshold."
        )


    explanation = {


        "summary":

        f"The candidate achieved {match_score}% compatibility. "
        "The score is calculated using skill similarity, "
        "experience, education and location factors.",


        "matched_skills":

        matched_skills,


        "missing_skills":

        missing_skills,


        "score_breakdown":

        {

            "skill_similarity":

            match_score,


            "experience_match":

            0,


            "education_match":

            0,


            "location_match":

            0

        },


        "recommendation":

        recommendation,


        "shortlisting_decision":

        {

            "status":

            status,


            "reason":

            reason

        }


    }


    return explanation