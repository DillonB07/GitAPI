import requests
import json

URL = 'https://api.github.com/graphql'

class ArgumentError(Exception):
    pass


class QueryFailError(Exception):
    pass


def get_query(self, query):
    request = requests.post(URL, json={'query': query}, headers=self.headers)
    if request.status_code == 200:
        return json.dumps(request.json(), indent=4, sort_keys=True)
    else:
        raise QueryFailError("Query failed to run by returning code of {}. {}".format(
            request.status_code, query))
