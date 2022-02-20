import requests
import json
import sys

__version__ = "1.0.0"


URL = "https://api.github.com/graphql"


class ArgumentError(Exception):
    pass


class QueryFailError(Exception):
    pass


def get_query(headers: dict, query: str):
    request = requests.post(URL, json={"query": query}, headers=headers)
    if request.status_code != 200:
        raise QueryFailError(
            "Query failed to run by returning code of {}. {}".format(
                request.status_code, query
            )
        )
    response = json.JSONDecoder().decode(json.dumps(request.json(), sort_keys=True))
    try:
        return response['data']
    except KeyError:
        return response


def check_alerts():
    py_version = sys.version
    # response = requests.get(f'https://git-api-alerts.dillonb07.repl.co/?py_version={py_version}&gitapi_version={__version__}').json()
