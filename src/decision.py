def shortlist_decision(score, matched):


    if len(matched) == 0:

        return {

            "status": "Rejected",

            "reason": "No required skills matched."

        }



    if score >= 55:

        return {

            "status": "Shortlisted",

            "reason": "Strong skill alignment found."

        }



    elif score >= 30:

        return {

            "status": "Review Required",

            "reason": "Candidate has partial skill alignment and should be reviewed."

        }



    else:

        return {

            "status": "Rejected",

            "reason": "Candidate does not meet minimum skill threshold."

        }