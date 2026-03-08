# GitHub API Testing

> This project showcases the CRUD workflow while testing the GitHub API. 

## Features:
- **API Testing**: Positive and negative tests coverage using [requests](https://requests.readthedocs.io/en/latest/) to interact with the GitHub API, handling all HTTP methods for data retrieval and submission
- **Test Suite Management**: Using the [pytest](https://docs.pytest.org/en/stable/getting-started.html) framework to organize the test suite and handle complex setups through fixtures
- **Schema Validation**: Ensure the API responses match the defined data models using [pydantic](https://docs.pydantic.dev/latest/) for schema validation
- **Security**: Using [python-dotenv](https://pypi.org/project/python-dotenv/) to manage the sensitive data such as the GitHub credentials, ensuring they remain excluded from version control.
- **CI/CD**: Fully integrated with GitHub Actions ([docs](https://docs.github.com/en/actions))
- **Containerization**: Dockerized environment for consistent execution ([docker](https://docs.docker.com/))
- **Reports**: Using [pytest-html](https://pytest-html.readthedocs.io/en/latest/) and [pytest-md-report](https://pypi.org/project/pytest-md-report/)


## How to run using Docker (easiest way)

> The Docker image can be found at this [link](https://hub.docker.com/r/cojoman1/api_testing_github-api-tests)

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

> Alternatively you can skip creating the ```.env``` file and pass the variables directly into the powershell:

<h5 a><strong><code>powershell</code></strong></h5>


```sh
docker run -e AUTH_TOKEN="your_token" -e AUTH_USER="your_user" cojoman1/api_testing_github-api-tests
```

If you need to generate a token from GitHub, use [these](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) instructions.


## How to run locally

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

<h5 a><strong><code>powershell</code></strong></h5>


```sh
uv sync --frozen
```

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


> This uses `uv.lock` to recreate the virtual environment using the exact dependency versions from the lockfile.

### 5. Running the tests: 

### 5.1. Running a single test:

<h5 a><strong><code>powershell</code></strong></h5>

```sh
uv run pytest tests/test_401_invalid_token.py
```

### 5.2. Running the whole test suite:

<h5 a><strong><code>powershell</code></strong></h5>

```sh
uv run pytest
```

### 5.3. Running the test suite with reports:

The reports will be available at `root/test-results/`. Create the path using:

```sh
mkdir test-results
```

<h5 a><strong><code>powershell</code></strong></h5>

```sh
uv run pytest --md-report --md-report-output test-results/report.md --md-report-color never --html=test-results/report.html --self-contained-html
```
