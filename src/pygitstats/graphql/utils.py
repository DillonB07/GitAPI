import json
from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

URL = 'https://api.github.com/graphql'


class ArgumentError(Exception):
    pass


class QueryFailError(Exception):
    pass


def get_query(headers, query):
    transport = AIOHTTPTransport(
        url=URL, headers=headers)
    client = Client(transport=transport, fetch_schema_from_transport=True)
    query = gql(query)
    response = client.execute(query)
    return json.dumps(response, indent=4, sort_keys=True)