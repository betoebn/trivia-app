import requests


def get_questions():
    parameters = {
        "amount": 10,
        "type": "boolean",
    }
    response = requests.get(url="https://opentdb.com/api.php?", params=parameters)
    response.raise_for_status()
    results = response.json()["results"]
    return results


question_data = get_questions()
