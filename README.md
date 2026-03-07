<div style="text-align: center;">
<h3>GitHub API Testing</h3>
</div>

### This project showcases CRUD workflows while testing the GitHub API. 
It covers two main topics:
### *Positive workflows*
1. Create: POST /user/repos to create new repository
2. Read: GET /repos/{owner}/{repo} to verify it exists and has the correct settings
3. Update: PATCH /repos/{owner}/{repo} to change the description or visibility
4. Delete: DELETE /repos/{owner}/{repo} to clean up

Tests that cover this:
- `test_repo_workflow.py`
- `test_issue_workflow.py`
- `test_comment_workflow.py`

For more info, check the comments in each file.

### *Negative workflows*

1. 401 Unauthorized: Attempt a private action with an invalid token
2. 404 Not Found: Requesting a repository that doesn't exist
3. 422 Unprocessable entity: Trying to create a repository with a name that already exists

Tests that cover this:
- `test_401_invalid_token.py`
- `test_404_repo_not_found.py`
- `test_422_create_dupe_repo.py`
- `test_422_create_repo_without_name.py`

<div style="text-align: center"><h2><strong>Project setup</strong></h2></div><br>

For this project, I've used `uv` to create the `.venv` and handle the package installation. 
To install uv, check this [link](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer)

### 1. Initialize the project

Open a terminal window and run the following commands:

<h5 a><strong><code>terminal</code></strong></h5>

```
uv init project-name
cd project-name
```

### 2. Add dependencies

<h5 a><strong><code>terminal</code></strong></h5>

```
uv sync
```
This will use the dependencies listed inside `pyproject.toml`

or you could:

<h5 a><strong><code>terminal</code></strong></h5>

```
uv pip install -r requirements.txt
```

This will use `requirements.txt` instead of `pyproject.toml`

### 3. Configure the `.env` file

- Create a file named `.env` in the root directory and add your credentials:

<h5 a><strong><code>.env</code></strong></h5>

```
GITHUB_TOKEN=your_github_token
GITHUB_USERNAME=your_github_username
```
- Add `.env` to your `.gitignore` file to prevent it from being pushed to GitHub

<h5 a><strong><code>.gitignore</code></strong></h5>

```
.env
```

- Access the variables in your Python code:

<h5 a><strong><code>.py</code></strong></h5>

```python
import os
from dotenv import load_dotenv

load_dotenv()  # This searches for and loads the .env file

username = os.getenv("GITHUB_USERNAME")
token = os.getenv("GITHUB_TOKEN")
```

###### Check `root/api_clients/base_client.py` to see the real usage


### 4. Run a test

To run a test, you'll have to use the command `pytest [test-location]`

For example:

<h5 a><strong><code>terminal</code></strong></h5>

```
pytest tests/test_repo_workflow.py
```



<div style="text-align: center"><h2><strong>conftest.py</strong></h2></div><br>

This file contains fixtures that allow us to type less code inside the tests by writting a piece of code once and injecting it through methods arguments where needed.<br> 
These fixtures are also allowing us to handle the setup and the teardown automatically.<br>
For example: repo creation happens automatically at the beginning of the test and repo deletion occurs after the test ends, no matter if the test was successful or not.<br><br>


Here we inject the fixture `repo_client` into a test:

<h5 a><strong><code>test_repo_workflow.py</code></strong></h5>

```python
def test_create_and_delete_repo_workflow(repo_client):
```

###### Check `root/tests/test_repo_workflow.py`

### We used:
- [pytest](https://docs.pytest.org/en/stable/getting-started.html) to organize the test suite and handle complex setups through fixtures
- [pydantic](https://docs.pydantic.dev/latest/) for schema validation to ensure API responses match the defined data models
- [python-dotenv](https://pypi.org/project/python-dotenv/) to manage the sensitive data such as the GitHub credentials, ensuring they remain excluded from version control.
- [requests](https://requests.readthedocs.io/en/latest/) to interact with the GitHub API, handling all HTTP methods for data retrieval and submission