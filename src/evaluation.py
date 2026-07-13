from src.skills import extract_skills
from src.metrics import calculate_metrics
import random



def create_validation_data(
        resumes,
        jobs,
        sample_size=200
):


    y_true=[]

    y_pred=[]



    for i in range(sample_size):


        resume = resumes.iloc[
            random.randint(
                0,
                len(resumes)-1
            )
        ]


        job = jobs.iloc[
            random.randint(
                0,
                len(jobs)-1
            )
        ]



        resume_skills = extract_skills(
            resume["combined_text"]
        )


        job_skills = extract_skills(
            job["combined_text"]
        )



        if len(job_skills)==0:

            continue



        overlap = len(

            set(resume_skills)
            &
            set(job_skills)

        )



        # Real relevance label

        if overlap > 0:

            actual = 1

        else:

            actual = 0



        # Model prediction

        if overlap / len(job_skills) >= 0.3:

            prediction = 1

        else:

            prediction = 0



        y_true.append(actual)

        y_pred.append(prediction)



    return y_true,y_pred





def evaluate_model(
        resumes,
        jobs
):


    y_true,y_pred = create_validation_data(
        resumes,
        jobs
    )



    metrics = calculate_metrics(
        y_true,
        y_pred
    )


    metrics["validation_samples"] = len(y_true)



    return metrics