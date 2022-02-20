---
description: HubAPI is the class that interacts with GitHub's API.
---

# HubAPI

### `HubAPI(token: str)`:

{% code title="main.py" %}
```python
from pygitapi import HubAPI

h = HubAPI('PERSONAL_ACCESS_TOKEN')
```
{% endcode %}

The `HubAPI` requires one parameter which is your personal access token as a string.

### `custom_query(self, query: str)`

The `custom_query()` function takes in one required parameter which is the GitHub GraphQL query. The function will return the output from GitHub as a Python dictionary.\
\
Learn more about GraphQL on the GitHub documentation - [https://docs.github.com/en/graphql/guides/introduction-to-graphql](https://docs.github.com/en/graphql/guides/introduction-to-graphql)

### `user_info(self, user: str)`

`user_info()` has one required parameter which is the user of the person you would like the data for. This function returns a collection of information about the user in a Python dictionary. Here's the data that's returned:

```json
{
    "user": {
        "avatarUrl": "https://avatars.githubusercontent.com/u/83948303?v=4",
        "bio": "An aspiring web developer who likes making weird and useless projects",
        "company": "Replit Coder | Hobby Coder",
        "email": "dillonbarnes07@gmail.com",
        "followers": {
            "totalCount": 7
        },
        "following": {
            "totalCount": 17
        },
        "isCampusExpert": false,
        "isDeveloperProgramMember": true,
        "issues": {
            "totalCount": 60
        },
        "itemShowcase": {
            "hasPinnedItems": true,
            "items": {
                "nodes": [
                    {
                        "name": "GitAPI"
                    },
                    {
                        "name": "Portfolio"
                    },
                    {
                        "name": "QAPI"
                    },
                    {
                        "name": "Dizzle"
                    },
                    {
                        "name": "Spotter"
                    },
                    {
                        "name": "FlaskBoilerplate"
                    }
                ]
            }
        },
        "location": "GMT, Leicester",
        "login": "DillonB07",
        "name": "Dillon Barnes",
        "organizations": {
            "nodes": [],
            "totalCount": 0
        },
        "pullRequests": {
            "totalCount": 38
        },
        "repositories": {
            "totalCount": 41
        },
        "starredRepositories": {
            "totalCount": 76
        },
        "status": null,
        "twitterUsername": null,
        "url": "https://github.com/DillonB07",
        "websiteUrl": "https://dillonb07.is-a.dev"
    }
}
```

You can then access the information you want like you would with a normal Python dictionary.\
`response['user']['login']` will return the user's username. This is completely pointless though as you will know this to be able to send the query. If a value is `null` then it will be returned as `None`.

### `repo_info(owner: str, name: str)`

`repo_info()` has two required parameters which are the owner and the name of the repository you would like the data for. This function returns a collection of information about the repository in a Python dictionary. Here's the data that's returned:

````json
{
    "repository": {
        "collaborators": null,
        "description": "A python wrapper for GitHub API",
        "forkCount": 1,
        "forkingAllowed": true,
        "homepageUrl": "https://docs.pygitapi.cf",
        "isArchived": false,
        "isEmpty": false,
        "isFork": false,
        "isInOrganization": false,
        "isPrivate": false,
        "issues": {
            "nodes": [
                {
                    "author": {
                        "avatarUrl": "https://avatars.githubusercontent.com/u/83948303?v=4",
                        "login": "DillonB07",
                        "url": "https://github.com/DillonB07"
                    },
                    "body": "The response returned by the `requests.post()` is of type `str` not `dict` meaning it can't be iterated through.",
                    "closedAt": "2022-01-10T18:10:35Z",
                    "createdAt": "2022-01-06T19:08:45Z",
                    "state": "CLOSED",
                    "title": "GraphQL response is `str` not `dict`",
                    "url": "https://github.com/DillonB07/GitAPI/issues/3"
                },
                {
                    "author": {
                        "avatarUrl": "https://avatars.githubusercontent.com/u/83948303?v=4",
                        "login": "DillonB07",
                        "url": "https://github.com/DillonB07"
                    },
                    "body": "* [x] *Possibly rename module back over to `pygitapi`? This would be better sooner rather than later.*\r\n* [ ] Add GraphQL mutations for functions like commenting on issues, reacting etc.\r\n\r\n\r\n---\r\n\r\nThis issue will also be used for testing mutations\r\n> ## **_WARNING: You probably don't want to follow this thread!_**\r\nIf anyone would like to reach me in this thread, please make sure to @DillonB07. Don't just leave a comment!",
                    "closedAt": "2022-01-29T16:40:26Z",
                    "createdAt": "2022-01-15T18:51:15Z",
                    "state": "CLOSED",
                    "title": "Add GraphQL mutation functions",
                    "url": "https://github.com/DillonB07/GitAPI/issues/7"
                },
                {
                    "author": {
                        "avatarUrl": "https://avatars.githubusercontent.com/u/83948303?v=4",
                        "login": "DillonB07",
                        "url": "https://github.com/DillonB07"
                    },
                    "body": "Documentation will be needed. Ideally with Sphinx though MkDocs is also fine.\r\n\r\nI'm not good at Sphinx...\r\n\r\n*All contributions for documentation are welcome! Credit will be added to README according to the [`All Contributors specification`](https://allcontributors.org/docs/en/specification)*\r\n",
                    "closedAt": null,
                    "createdAt": "2022-01-20T17:54:33Z",
                    "state": "OPEN",
                    "title": "Documenation",
                    "url": "https://github.com/DillonB07/GitAPI/issues/13"
                },
                {
                    "author": {
                        "avatarUrl": "https://avatars.githubusercontent.com/u/83948303?v=4",
                        "login": "DillonB07",
                        "url": "https://github.com/DillonB07"
                    },
                    "body": "```py\r\n{'errors': [{'extensions': {'code': 'undefinedField', 'fieldName': 'body', 'typeName': 'IssueCommentEdge'}, 'locations': [{'column': 13, 'line': 5}], 'message': \"Field 'body' doesn't exist on type 'IssueCommentEdge'\", 'path': ['mutation', 'addComment', 'commentEdge', 'body']}]}\r\n```\r\n\r\n",
                    "closedAt": "2022-01-20T18:30:30Z",
                    "createdAt": "2022-01-20T18:29:10Z",
                    "state": "CLOSED",
                    "title": "Error in `v1.0.0rc5` - field `body` doesn't exist",
                    "url": "https://github.com/DillonB07/GitAPI/issues/15"
                },
                {
                    "author": {
                        "avatarUrl": "https://avatars.githubusercontent.com/u/83948303?v=4",
                        "login": "DillonB07",
                        "url": "https://github.com/DillonB07"
                    },
                    "body": "GitLab API integration is planned and will be coming soon...\r\n\r\n<!-- Edit the body of your new issue then click the \u2713 \"Create Issue\" button in the top right of the editor. The first line will be the issue title. Assignees and Labels follow after a blank line. Leave an empty line before beginning the body of the issue. -->",
                    "closedAt": null,
                    "createdAt": "2022-01-29T16:36:27Z",
                    "state": "OPEN",
                    "title": "GitLab API Integration",
                    "url": "https://github.com/DillonB07/GitAPI/issues/18"
                },
                {
                    "author": {
                        "avatarUrl": "https://avatars.githubusercontent.com/u/83948303?v=4",
                        "login": "DillonB07",
                        "url": "https://github.com/DillonB07"
                    },
                    "body": "BitBucket API integration is planned and will be coming soon...\n\n> NOTE: BitBucket is still using REST endpoints, not GraphQL.\n\n<!-- Edit the body of your new issue then click the \u2713 \"Create Issue\" button in the top right of the editor. The first line will be the issue title. Assignees and Labels follow after a blank line. Leave an empty line before beginning the body of the issue. -->",
                    "closedAt": null,
                    "createdAt": "2022-01-29T16:38:46Z",
                    "state": "OPEN",
                    "title": "BitBucket API Integration",
                    "url": "https://github.com/DillonB07/GitAPI/issues/19"
                }
            ],
            "totalCount": 6
        },
        "nameWithOwner": "DillonB07/GitAPI",
        "stargazerCount": 3,
        "stargazers": {
            "nodes": [
                {
                    "avatarUrl": "https://avatars.githubusercontent.com/u/83948303?v=4",
                    "login": "DillonB07",
                    "name": "Dillon Barnes",
                    "url": "https://github.com/DillonB07"
                },
                {
                    "avatarUrl": "https://avatars.githubusercontent.com/u/76911308?u=2f9828c39201bc4b575b6c4f1042f8f622038c7b&v=4",
                    "login": "kokonut27",
                    "name": "kokomi simp :3",
                    "url": "https://github.com/kokonut27"
                },
                {
                    "avatarUrl": "https://avatars.githubusercontent.com/u/60611498?u=8adc81a71b36953d94cbc9fd441ab9db8a8eab08&v=4",
                    "login": "sourcery-ai-bot",
                    "name": "Sourcery AI",
                    "url": "https://github.com/sourcery-ai-bot"
                }
            ]
        },
        "updatedAt": "2022-02-13T17:18:18Z",
        "url": "https://github.com/DillonB07/GitAPI",
        "viewerCanAdminister": false,
        "viewerHasStarred": false,
        "watchers": {
            "nodes": [
                {
                    "avatarUrl": "https://avatars.githubusercontent.com/u/83948303?v=4",
                    "login": "DillonB07",
                    "name": "Dillon Barnes",
                    "url": "https://github.com/DillonB07"
                }
            ]
        }
    }
}
````

You can then access the information you want like you would with a normal Python dictionary.\
`response['repository']['homepageUrl']` will return the repository's website.  If a value is `null` then it will be returned as `None`.

### `get_issue_id(owner: str, repo: str, number: int)`

`get_issue_id()` quite simply gets the id of the issue specified.\
For example, `get_issue_id('DillonB07', 'GitAPI', 19)` returns `I_kwDOGn7mEc5Cp2Qc`.\
This is mainly for use with custom queries and is used by `comment_on_issue()`.

### `comment_on_issue(owner: str, repo: str, number: int, comment: str)`

`comment_on_issue()` adds a comment to the issue you provide. \
If I run `comment_on_issue('DillonB07', 'GitAPI', 7, 'This was sent from a demo program')` it will comment on the specified issue and return the following:

```json
{
    "addComment": {
        "commentEdge": {
            "node": {
                "body": "This was sent from a demo program"
            }
        }
    }
}
```
