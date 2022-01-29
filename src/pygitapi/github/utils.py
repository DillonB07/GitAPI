import requests
import json

URL = 'https://api.github.com/graphql'


class ArgumentError(Exception):
    pass


class QueryFailError(Exception):
    pass


def get_query(headers: dict, query: str):
    request = requests.post(
        URL, json={'query': query}, headers=headers)
    if request.status_code == 200:
        return json.JSONDecoder().decode(json.dumps(request.json(), sort_keys=True))
    else:
        raise QueryFailError("Query failed to run by returning code of {}. {}".format(
            request.status_code, query))
