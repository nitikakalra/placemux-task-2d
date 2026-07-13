import os
import json


def save_json(data, filename):

    folder = os.path.dirname(filename)


    if folder:

        os.makedirs(
            folder,
            exist_ok=True
        )


    with open(filename, "w") as file:

        json.dump(
            data,
            file,
            indent=4
        )


    print(
        f"Saved: {filename}"
    )