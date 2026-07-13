from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity



class JobMatcher:


    def __init__(self):

        self.vectorizer = TfidfVectorizer(
            stop_words="english"
        )



    def fit(self, jobs):

        self.job_vectors = self.vectorizer.fit_transform(
            jobs
        )



    def match(self, resume_text, jobs):

        resume_vector = self.vectorizer.transform(
            [resume_text]
        )


        scores = cosine_similarity(
            resume_vector,
            self.job_vectors
        )[0]


        results=[]


        for index,score in enumerate(scores):

            results.append({

                "job_id":index,

                "match_score":
                round(float(score*100),2)

            })


        results = sorted(
            results,
            key=lambda x:x["match_score"],
            reverse=True
        )


        return results[:10]