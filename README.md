<div style="text-align: center;">
<h3>GitHub API Testing</h3>
</div>

### This project showcases the CRUD workflow while testing the GitHub API. 
It covers both positive and negative tests. For more info check the test files at: 

```root/tests/```

<div style="text-align: center"><h2><strong>Run locally</strong></h2></div><br>

For this project, I've used `uv`. 
To install `uv`, follow the steps from this [link](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer)

If you want to run this locally, follow these steps (for Windows):

### 1. Download the project ZIP and extract it
### 2. Navigate into the root project directory and open a terminal here
- Shift+Right Click > Open in Terminal
  <br>or
- Navigate here using the Terminal


### 3. Initialize the project

In the terminal window run the following command:

<h5 a><strong><code>terminal</code></strong></h5>


```
uv sync
```
This will use the dependencies listed inside `pyproject.toml`




### 4. Configure the `.env` file

- Create a file named `.env` in the root directory and add your credentials:

<h5 a><strong><code>.env</code></strong></h5>

```
AUTH_TOKEN=your_github_token
AUTH_USER=your_github_username
```
You need to generate a token from GitHub using [these](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) steps

- Add `.env` to your `.gitignore` file to prevent it from being pushed to GitHub

<h5 a><strong><code>.gitignore</code></strong></h5>

```
.env
```

### 5. Run the test suite

<h5 a><strong><code>terminal</code></strong></h5>

```
uv run pytest
```



To run a single test:

<h5 a><strong><code>terminal</code></strong></h5>

```
uv run pytest tests/test_repo_workflow.py
```



To run tests with reports:

<h5 a><strong><code>terminal</code></strong></h5>

```
uv run pytest --md-report --md-report-output reports/report.md --md-report-color never --html=reports/report.html --self-contained-html
```


The reports will be available at ```root/reports/```. Make sure the path exists before running the command.

<div style="text-align: center"><h2><strong>conftest.py</strong></h2></div><br>

This file contains fixtures that allow us to type less code inside the tests by writting a piece of code once and injecting it through methods arguments where needed.<br> 
These fixtures are also allowing us to handle the setup and the teardown automatically.<br>
For example: repo creation happens automatically at the beginning of the test and repo deletion occurs after the test ends, no matter if the test was successful or not.<br><br>


Here we inject the fixture `repo_client` into a test:

<h5 a><strong><code>test_repo_workflow.py</code></strong></h5>

```python
def test_create_and_delete_repo_workflow(repo_client):
```

###### Check `root/tests/test_repo_workflow.py` to see the real usage.

### What this uses:
- [pytest](https://docs.pytest.org/en/stable/getting-started.html) to organize the test suite and handle complex setups through fixtures
- [pydantic](https://docs.pydantic.dev/latest/) for schema validation to ensure API responses match the defined data models
- [python-dotenv](https://pypi.org/project/python-dotenv/) to manage the sensitive data such as the GitHub credentials, ensuring they remain excluded from version control.
- [requests](https://requests.readthedocs.io/en/latest/) to interact with the GitHub API, handling all HTTP methods for data retrieval and submission
- [pytest-html](https://pytest-html.readthedocs.io/en/latest/) for detailed reports
- [pytest-md-report](https://pypi.org/project/pytest-md-report/) for simple reports