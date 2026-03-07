from uuid import uuid4

import pytest

from api_clients.repo_client import RepoClient


# Using this to make our test modular - it will test all these cases without having us repeat the code for each case
# We're passing these parameters into the function below
@pytest.mark.parametrize(
    "repo_name, expected_status",
    [
        (
            f"non-existent-{uuid4().hex[:6]}",
            404,
        ),  # Case 1: Valid format with non-existent repo name
        ("!", 404),  # Case 2: Invalid characters
        ("", 404),  # Case 3: Empty name
        ("a" * 101, 404),  # Case 4: Name too long
    ],
)
def test_get_repo_invalid_cases(repo_client: RepoClient, repo_name, expected_status):
    """Test invalid GETs for repositories"""
    owner = repo_client.username

    get_res = repo_client.get_repository(owner, repo_name)

    assert get_res.status_code == expected_status

    print(
        f"get_repository({repo_name[:6]}) response: {get_res.status_code}; Expected: {expected_status}"
    )
