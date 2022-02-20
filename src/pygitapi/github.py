from .utils import get_query


class HubAPI:
    """Use GitHub's GraphQL API to get information about repositories, users and more"""

    def __init__(self, token: str):
        """Hold GitHub token"""
        self.token = token
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

        return self.custom_query(query)

    def repo_info(self, owner: str, name: str):
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

        return self.custom_query(query)

    def get_issue_id(self, owner: str, repo: str, number: int):
        query = '''
query {
    repository(owner: "''' + owner + '''", name: "''' + repo + '''") {
        issue(number: ''' + str(number) + ''') {
            id
        }
    }
}
    '''
        response = self.custom_query(query)
        return response['repository']['issue']['id']

    def comment_on_issue(self, owner: str, repo: str, number: int, comment: str):
        id = self.get_issue_id(owner, repo, number)
        mutation = '''
mutation {
    addComment(input: {subjectId: "''' + id + '''", body: "''' + comment + '''"}) {
        commentEdge {
            node {
                body
            }
        }
    }
}
        '''

        return self.custom_query(mutation)
