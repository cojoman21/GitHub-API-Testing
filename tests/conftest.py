import os
from uuid import uuid4

import pytest

from api_clients.comment_client import CommentClient
from api_clients.issue_client import IssueClient
from api_clients.repo_client import RepoClient


## Base Fixtures
# Creates a repo
@pytest.fixture(scope="session")
def repo_client():
    return RepoClient()


# Tries to create a repo using an invalid Token
@pytest.fixture
def unauthorized_repo_client():
    return RepoClient(token="bad_token")


# Creates an issue
@pytest.fixture(scope="function")
def issue_client():
    return IssueClient()


# Creates a comment
@pytest.fixture(scope="function")
def comment_client():
    return CommentClient()


# Create multiple repos at once
@pytest.fixture
def multiple_repos(repo_client: RepoClient):
    repo_names = [f"pagin-test-{uuid4().hex[:4]}" for _ in range(3)]
    for name in repo_names:
        repo_client.create_repository(name)

    yield repo_names

    for name in repo_names:
        repo_client.delete_with_retry(repo_client.username, name)


## Temp fixtures
# Creates a temporary repo (setup) and deletes it after the test is complete (teardown)
@pytest.fixture(scope="function")
def temp_repo(repo_client):
    name: str = f"test-repo-{uuid4().hex[:6]}"
    repo_client.create_repository(name)

    yield name

    repo_client.delete_with_retry(os.getenv("GITHUB_USERNAME"), name)


# Creates a temporary issue (setup) and deletes it (sets state="closed") after the test is complete (teardown)
@pytest.fixture(scope="function")
def temp_issue(issue_client: IssueClient, temp_repo_name: str):
    repo_name = temp_repo_name
    owner = RepoClient().username

    response = issue_client.create_issue(
        owner, repo_name, title="Test issue", body="Steps to repro"
    )

    issue_data = response.json()
    issue_number: int = issue_data["number"]

    yield issue_number
    issue_client.delete_issue(owner, repo_name, issue_number)


## Helper fixtures (used for best practices)
# Uses temp_repo and returns the repo name as str
@pytest.fixture
def temp_repo_name(temp_repo) -> str:
    return temp_repo


@pytest.fixture
def temp_issue_number(temp_issue) -> int:
    return temp_issue


# Mock data
@pytest.fixture(scope="function")
def limit_reached_data():
    return {
        "x-ratelimit-limit": "60",
        "x-ratelimit-remaining": "0",
        "x-ratelimit-used": "60",
        "x-ratelimit-reset": "99999999",
        "x-ratelimit-resource": "core",
    }
