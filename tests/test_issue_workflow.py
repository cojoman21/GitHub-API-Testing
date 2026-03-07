from api_clients.issue_client import IssueClient
from api_clients.repo_client import RepoClient

"""
This test showcases the CRUD workflow for a GitHub repo issue
"""


def test_issue_workflow(
    repo_client: RepoClient, temp_repo_name: str, issue_client: IssueClient
):
    """Test the CRUD workflow for a GitHub issue on a repository"""
    # temp_repo_name uses the temp_repo fixture to create the repo and yield the name as str
    repo_name = temp_repo_name
    # GitHub token
    owner = repo_client.username

    ## 1. Create/POST an issue and check if the operation was successful
    issue_res = issue_client.create_issue(
        owner, repo_name, "Found a bug", "Steps to repro"
    )
    assert issue_res.status_code == 201

    print(f"create_issue() response: {issue_res.status_code}")

    # Extract the issue number
    issue_number = issue_res.json()["number"]

    ## 2. Read/GET the issue and check if the operation was successful
    get_res = issue_client.get_issue(owner, repo_name, issue_number)
    assert get_res.status_code == 200
    assert get_res.json()["title"] == "Found a bug"

    print(f"get_issue() response: {get_res.status_code}")

    ## 3. Update/PATCH the issue and check if the operation was successful
    update_res = issue_client.update_issue(
        owner, repo_name, issue_number, new_title="Updated Issue Title"
    )
    assert update_res.status_code == 200
    assert update_res.json()["title"] == "Updated Issue Title"

    # Read/GET again on the updated issue
    get_res = issue_client.get_issue(owner, repo_name, issue_number)
    assert get_res.status_code == 200
    assert get_res.json()["title"] == "Updated Issue Title"

    ## 4. Delete/PATCH the issue and check if the operation was successful
    # We set the issue status to "closed" since we can't actually delete it
    close_res = issue_client.delete_issue(owner, repo_name, issue_number, "closed")

    assert close_res.status_code == 200
    assert close_res.json()["state"] == "closed"


# The repo goes out of scope and gets automatically deleted here
