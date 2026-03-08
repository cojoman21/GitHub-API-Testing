<div style="text-align: center;">
<h2><strong>GitHub API Testing</strong></h2>
</div>

### This project showcases the CRUD workflow while testing the GitHub API. 
It covers both positive and negative tests. For more info check the test files at: 

```root/tests/```

<div style="text-align: center"><h2><strong>Running locally</strong></h2></div><br>

For this project, I've used `uv`. 
To install `uv`, follow the steps from this [link](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer)

If you want to run this locally, follow these steps (for Windows):

### 1. Open a powershell window and download the project using:

<h5 a><strong><code>powershell</code></strong></h5>

```sh
git clone https://github.com/cojoman21/GitHub-API-Testing.git
```

#### Alternatively you can manually download the repository from this [link](https://github.com/cojoman21/GitHub-API-Testing)

### 2. Navigate into the root project directory 


<h5 a><strong><code>powershell</code></strong></h5>

```sh
cd GitHub-API-Testing
```


### 3. Initialize the project

In the powershell window run the following command:

<h5 a><strong><code>powershell</code></strong></h5>


```sh
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

### Running the whole test suite

<h5 a><strong><code>powershell</code></strong></h5>

```sh
uv run pytest
```



### Running a single test:

<h5 a><strong><code>powershell</code></strong></h5>

```sh
uv run pytest tests/test_repo_workflow.py
```



### Running the tests with reports:

The reports will be available at ```root/reports/```. Make sure the path exists before running the command.

```sh
mkdir reports
```

<h5 a><strong><code>powershell</code></strong></h5>

```sh
uv run pytest --md-report --md-report-output reports/report.md --md-report-color never --html=reports/report.html --self-contained-html
```

<div style="text-align: center"><h2><strong>Running with docker</strong></h2></div><br>

The Docker image can be found at this [link](https://hub.docker.com/r/cojoman1/api_testing_github-api-tests)

### 1. Open a powershell window and run:

<h5 a><strong><code>powershell</code></strong></h5>

```sh
docker pull cojoman1/api_testing_github-api-tests
```

### 2. Create a ```.env``` file that contains the GitHub Token and Username

<h5 a><strong><code>.env</code></strong></h5>

```
AUTH_TOKEN=your_github_token
AUTH_USER=your_github_username
```


### 3. Open a powershell at the location of the ```.env``` file and run:

<h5 a><strong><code>powershell</code></strong></h5>

```sh
docker run --env-file .env cojoman1/api_testing_github-api-tests
```

#### Alternatively you can skip creating the ```.env``` file and pass the variables directly into the powershell:

<h5 a><strong><code>powershell</code></strong></h5>


```sh
docker run -e AUTH_TOKEN="your_token" -e AUTH_USER="your_user" cojoman1/api_testing_github-api-tests
```

If you need to generate a token from GitHub, use [these](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) instructions.

<br>

<div style="text-align: center"><h2><strong>About the project</strong></h2></div><br>

### What it uses:
* [pytest](https://docs.pytest.org/en/stable/getting-started.html) to organize the test suite and handle complex setups through fixtures
* [pydantic](https://docs.pydantic.dev/latest/) for schema validation to ensure API responses match the defined data models
* [python-dotenv](https://pypi.org/project/python-dotenv/) to manage the sensitive data such as the GitHub credentials, ensuring they remain excluded from version control.
* [requests](https://requests.readthedocs.io/en/latest/) to interact with the GitHub API, handling all HTTP methods for data retrieval and submission
* [pytest-html](https://pytest-html.readthedocs.io/en/latest/) for detailed reports
* [pytest-md-report](https://pypi.org/project/pytest-md-report/) for simple reports

<br>

* The API Clients are stored at ```root/api_clients/```.
* The Pydantic validation models are stored in ```root/models/base_model.py```
* The tests are stored in ```root/tests/```
  * ```conftest.py``` can also be found there <br>
This file contains fixtures that help avoid repeating setup code inside the tests by writing a piece of code once and injecting it through methods arguments where needed.<br> 
These fixtures also handle the setup and the teardown automatically.<br>
For example: repo creation happens automatically at the beginning of the test and repo deletion occurs after the test ends, regardless of whether the test passes or fails.<br><br>
Here we inject the fixture `repo_client` into ```test_repo_workflow.py```:
    ```python
    def test_create_and_delete_repo_workflow(repo_client):
    ```
    Check `root/tests/test_repo_workflow.py` to see the real usage.
* ```.github/workflows/python-tests.yml``` contains the GitHub Action workflow file that runs the tests on every push/pull and it also allows manually running the tests
* ```.env.example``` is an example file showing how your ```.env``` should look like