---
description: Follow along to access basic user data from GitHub via the GitAPI package.
---

# GitHub - Accessing user data

One of the most useful features of this module is being able to get readily available user data with one simple function. You don't need to mess around with complicated queries as they're built in for you!

### Creating a Personal Access Token

In order to access information from GitHub, you need a Personal Access Token. Let's create one!

1. Go to [https://github.com/settings/tokens](https://github.com/settings/tokens) and sign in. You should be greeted with a screen like this.
2. Click `Generate new token` , sign in and call the token GitAPI. If you want, you can set an expiration date or leave it as `No expiration` . &#x20;
3. For your scopes, you'll want `read:user` and `read:org`. If you want, you can add extra scopes depending on what you are doing with the API. However, you should only add the scopes that you need.
4. Your token has been created. It should be shown to you like this:

![](../.gitbook/assets/personal\_access\_token.png)

{% hint style="danger" %}
Make sure that you do not share your token or publish it online. If anyone else gets access to your token, they can use your GitHub account with the permissions attached to the token. If you accidentally share it, go to the tokens page and revoke it immediately.
{% endhint %}

### Creating a basic program

Open the environment we created in the previous guide and create a file called `main.py` with the following code:

{% hint style="warning" %}
Make sure that you don't keep your token in your code. You should use environmental variables to hold your tokens. It's ok to put it in your code for testing.
{% endhint %}

{% code title="main.py" %}
```python
from pygitapi import HubAPI
import json

h = HubAPI('PERSONAL ACCESS TOKEN')
user_info = h.user_info('DillonB07')

print(json.dumps(user_info, indent=4))
```
{% endcode %}

This code will output the following when run in the environment we created:

{% hint style="info" %}
The `json.dumps()` is not necessary. I've used this to make the output more readable. However, this also converts it to a string so you won't want this in the majority of programs.
{% endhint %}

```json
{
    "data": {
        "user": {
            "avatarUrl": "https://avatars.githubusercontent.com/u/83948303?v=4",
            "bio": "An aspiring web developer who likes making weird and useless projects",
            "company": "Replit Coder | Hobby Coder",
            "email": "dillonbarnes07@gmail.com",
            "followers": {
                "totalCount": 6
            },
            "following": {
                "totalCount": 17
            },
            "isCampusExpert": false,
            "isDeveloperProgramMember": true,
            "issues": {
                "totalCount": 58
            },
            "itemShowcase": {
                "hasPinnedItems": true,
                "items": {
                    "nodes": [
                        {
                            "name": "Portfolio"
                        },
                        {
                            "name": "Spotter"
                        },
                        {
                            "name": "FlaskBoilerplate"
                        },
                        {
                            "name": "Dizzle"
                        },
                        {
                            "name": "QAPI"
                        },
                        {
                            "name": "theiolang.github.io"
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
                "totalCount": 36
            },
            "repositories": {
                "totalCount": 40
            },
            "starredRepositories": {
                "totalCount": 72
            },
            "status": null,
            "twitterUsername": null,
            "url": "https://github.com/DillonB07",
            "websiteUrl": "https://dillonb07.is-a.dev"
        }
    }
}
```

You can get specific user data like so:

```python
...
user_info = h.user_info('DillonB07')['data']['user']['bio']
print(user_info)
```

This will print out the user's bio.

```shell
An aspiring web developer who likes making weird and useless projects
```

