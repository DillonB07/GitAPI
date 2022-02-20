---
description: Default functions not working for you? Use custom queries!
---

# GitHub - Using custom queries

The `HubAPI.custom_query()` function lets you specify a custom query!

Here's an example:

{% hint style="info" %}
GitHub uses GraphQL which is a type of API developed by ~~Facebook~~ Meta.&#x20;

Learn more about GitHub and GraphQL here - [https://docs.github.com/en/graphql/overview/about-the-graphql-api](https://docs.github.com/en/graphql/overview/about-the-graphql-api)
{% endhint %}

{% code title="main.py" %}
```python
from pygitapi import HubAPI



token = 'PERSONAL ACCESS TOKEN'

h = HubAPI(token)

query = """
query {
    user(login: "DillonB07") {
        name
    }
}
"""

print(h.custom_query(query))
```
{% endcode %}

This will return:

```
{'user': {'name': 'Dillon Barnes'}}
```

{% hint style="success" %}
Create your own queries using GitHub's [GraphiQL explorer](https://docs.github.com/en/graphql/overview/explorer)
{% endhint %}
