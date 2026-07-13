import json



def save_dataset_summary(
        jobs,
        resumes
):


    summary={


        "total_jobs":
        len(jobs),


        "total_resumes":
        len(resumes),


        "purpose":
        "Real shaped dataset used for explainable job matching"

    }



    with open(
        "outputs/dataset_summary.json",
        "w"
    ) as f:


        json.dump(
            summary,
            f,
            indent=4
        )