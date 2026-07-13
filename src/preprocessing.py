import pandas as pd
import re



def clean_text(text):

    if pd.isna(text):

        return ""

    text = str(text).lower()

    text = re.sub(
        r'[^a-zA-Z0-9+#\s]',
        ' ',
        text
    )

    return text




def load_jobs(
        path="data/jobs.csv"
):

    df=pd.read_csv(path)

    df=df.fillna("")

    return df





def load_resumes(
        path="data/resumes.csv"
):

    df=pd.read_csv(path)

    df=df.fillna("")

    return df





def prepare_job_text(row):


    text = (

        str(row["job_title"])
        +
        " "
        +
        str(row["job_description"])
        +
        " "
        +
        str(row["job_skill_set"])

    )


    return clean_text(text)





def prepare_resume_text(row):


    text = str(
        row["Resume_str"]
    )


    return clean_text(text)