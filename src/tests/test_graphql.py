import pytest
from pygitapi.github import HubAPI
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
token = os.environ['PERSONAL_ACCESS_TOKEN']
g = HubAPI(token)


def test_user_info():
    response = g.user_info('DillonB07')
    if response['data']['user']['login'] == 'DillonB07':
        output = True
    else:
        output = False
    assert output == True


def test_repo_info():
    response = g.repo_info(owner='DillonB07', name='GitAPI')
    if response['data']['repository']['nameWithOwner'] == 'DillonB07/GitAPI':
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
    if response['data']['user']['login'] == 'DillonB07' and response['data']['user']['url'] == 'https://github.com/DillonB07':
        output = True
    else:
        print(response)
        output = False
    assert output == True


def test_get_issue_id():
    response = g.get_issue_id('DillonB07', 'GitAPI', 7)
    assert response == 'I_kwDOGn7mEc5B2iR3'


def test_comment_on_issue():
    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    response = g.comment_on_issue(
        'DillonB07', 'GitAPI', 7, f'Test `test_comment_on_issue()` ran successfully at {current_time}')
    assert response == {'data': {'addComment': {'commentEdge': {'node': {
        'body': f'Test `test_comment_on_issue()` ran successfully at {current_time}'}}}}}


def test_custom_mutation():
    query = '''
query {
  repository(owner: "DillonB07", name: "GitAPI") {
    issue(number: 7) {
      id
    }
  }
}
    '''
    id_response = g.custom_query(query)
    id = id_response['data']['repository']['issue']['id']
    time = datetime.now()
    current_time = time.strftime("%d-%m-%Y %H:%M:%S")
    mutation = '''
mutation {
  addComment(input: {subjectId: "''' + id + '''", body: "Test `test_custom_mutation()` ran successfully at ''' + current_time + '''"}) {
    commentEdge {
        node {
            body
        }
    }
  }
}
    '''
    response = g.custom_query(mutation)
    print(response)

    assert response == {'data': {'addComment': {'commentEdge': {'node': {
        'body': f'Test `test_custom_mutation()` ran successfully at {current_time}'}}}}}
