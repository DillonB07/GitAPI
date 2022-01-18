from .utils import get_query


class GitAPI:
    """Use GitHub's GraphQL API to get information about repositories, users and more"""

    def __init__(self, git_token: str):
        """Hold GitHub token"""
        self.token = git_token
        self.headers = {"Authorization": f"Bearer {self.token}"}

    def custom_query(self, query: str):
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
    
    def repo_info(self, name: str, owner: str):
        """Returns basic information about given repositor"""
        query = """
query {
  repository(name: \"""" + name + """\", owner: \"""" + owner + """\") {
    nameWithOwner
    url
    homepageUrl
    isInOrganization
    description
    stargazerCount
    stargazers(first: 10) {
      nodes {
        login
        name
        avatarUrl
        url
      }
    }
    watchers(first: 10) {
      nodes {
        login
        name
        avatarUrl
        url
      }
    }
    issues(first: 10) {
      totalCount
      nodes {
        author {
          login
          url
          avatarUrl
        }
        body
        url
        title
        state
        closedAt
        createdAt
      }
    }
    updatedAt
    viewerCanAdminister
    viewerHasStarred
    collaborators(first: 10) {
      totalCount
      nodes {
        avatarUrl
        login
        name
        url
      }
    }
    isEmpty
    isFork
    isArchived
    forkingAllowed
    forkCount
    isPrivate
  }
}

        """
        response = get_query(self.headers, query)
        return response
