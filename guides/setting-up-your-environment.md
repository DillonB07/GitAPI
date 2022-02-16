---
description: Learn how to setup your environment with the GitAPI module.
---

# Setting up your environment

## Dependencies

1. Python 3.6 or greater
2. Pip
3. Requests module - _This will automatically get installed with GitAPI_

## Setting up a project

Open up your Terminal and run the following commands after navigating to your project directory

{% hint style="warning" %}
If `python` or `pip` don't work, then try `python3` or `pip3`.&#x20;
{% endhint %}

```shell-session
python -m venv venv
source venv/bin/activate
pip install --upgrade pygitapi
```
