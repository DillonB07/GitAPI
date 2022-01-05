import requests
import json

URL = 'https://api.github.com/graphql'


class ArgumentError(Exception):
    pass


class QueryFailError(Exception):
    pass


class GitStats:
    """Use GitHub's GraphQL API to get information about repositories, users and more"""

    def __init__(self, git_token: str):
        self.token = git_token
        self.headers = {"Authorization": "Bearer " + self.token}

    def get_query(self, query):

        request = requests.post(
            URL, json={'query': query}, headers=self.headers)
        if request.status_code == 200:
            return json.dumps(request.json(), indent=4, sort_keys=True)
        else:
            raise QueryFailError("Query failed to run by returning code of {}. {}".format(
                request.status_code, query))

    def custom_query(self, query):
        """Allows usage of custom GraphQL queries for the GitHub GrapQL API"""
        return self.get_query(query)

    def user_info(self, user: str):
        """Returns basic information about given user"""
        query = '''
query user {
  user(login: "''' + user + '''") { 
    url
    login
    name
    twitterUsername
    websiteUrl
    email
    company
    location
    status {
      message
      indicatesLimitedAvailability
    }
    avatarUrl
    bio
    isDeveloperProgramMember
    isCampusExpert
    starredRepositories {
      totalCount
    }
    followers {
      totalCount
    }
    following {
      totalCount
    }
    issues {
      totalCount
    }
    pullRequests {
      totalCount
    }
    itemShowcase {
      hasPinnedItems
      items(first: 10) {
        nodes {
          ... on Repository {
            name
          }
        }
      }
    }
    organizations(first: 10) {
      totalCount
      nodes {
        name
      }
    }
    repositories {
      totalCount
    }
  }
}
        '''
        print(query)
        response = self.get_query(query)
        print(response)
