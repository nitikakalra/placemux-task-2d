import ast
import re



def extract_skills(text):


    if not isinstance(text, str):

        return []



    skills = []



    try:

        parsed = ast.literal_eval(text)


        if isinstance(parsed, list):


            for item in parsed:


                if isinstance(item, str):

                    clean = item.lower().strip()


                    if clean:

                        skills.append(clean)



            return list(set(skills))



    except (ValueError, SyntaxError):

        pass



    text = text.lower()



    common_skills = [

        "python",
        "java",
        "javascript",
        "react",
        "sql",
        "mysql",
        "mongodb",
        "aws",
        "docker",
        "kubernetes",
        "machine learning",
        "data analysis",
        "data science",
        "excel",
        "communication",
        "leadership",
        "project management",
        "html",
        "css",
        "git",
        "spark",
        "scala",
        "azure",
        "nosql"

    ]



    for skill in common_skills:


        if skill in text:

            skills.append(skill)



    return list(set(skills))