from .utils import get_query


class GitStats:
    """Use GitHub's GraphQL API to get information about repositories, users and more"""

    def __init__(self, git_token: str):
        """Hold GitHub token"""
        self.token = git_token
        self.headers = {"Authorization": f"Bearer {self.token}"}

    def custom_query(self, query):
        """Allows usage of custom GraphQL queries for the GitHub GraphQL API"""
        return get_query(self.headers, query)

    def user_info(self, user: str):
        """Returns basic information about given user"""
        query = """
query {
  user(login: \"""" + user + """\") { 
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
        """
        response = get_query(self.headers, query)
        return response
