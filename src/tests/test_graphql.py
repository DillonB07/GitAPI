import pytest
from pygitstats.graphql import GitStats
import os
from dotenv import load_dotenv

load_dotenv()
token = os.environ['GITHUB_PERSONAL_ACCESS_TOKEN']
g = GitStats(token)


def test_user_info():
    response = g.user_info('DillonB07')
    if response['user']['login'] == 'DillonB07':
        output = True
    else:
        output = False
    assert output == True


def test_custom_query():
    query = '''
query {
    user(login: "DillonB07") {
        url
        login
    }
}
    '''
    response = g.custom_query(query)
    if response['user']['login'] == 'DillonB07' and response['data']['user']['url'] == 'https://api.github.com/users/DillonB07':
        output = True
    else:
        output = False
    assert output == True
