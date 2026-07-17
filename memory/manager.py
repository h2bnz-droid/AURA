import json
import os

FILE_NAME = "memory/profile.json"


def load_profile():

    if not os.path.exists(FILE_NAME):

        return {
            "name": "",
            "nickname": "",
            "project": "AURA",
            "memories": []
        }

    with open(FILE_NAME, "r", encoding="utf-8") as f:

        return json.load(f)


def save_profile(profile):

    os.makedirs("memory", exist_ok=True)

    with open(FILE_NAME, "w", encoding="utf-8") as f:

        json.dump(profile, f, indent=4, ensure_ascii=False)