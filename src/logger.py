import json
from datetime import datetime



def save_experiment(metrics):


    data={

        "timestamp":
        str(datetime.now()),


        "experiment":
        "Explainable Job Matching",


        "metrics":
        metrics

    }


    with open(
        "outputs/experiment_log.json",
        "w"
    ) as f:

        json.dump(
            data,
            f,
            indent=4
        )