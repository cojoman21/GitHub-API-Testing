from api_clients.repo_client import RepoClient


def test_422_create_duplicate_repo(repo_client: RepoClient, temp_repo_name: str):
    """Test creating a repository with a name that is already used by another repository"""
    existent_repo = temp_repo_name
    create_res = repo_client.create_repository(name=existent_repo)

    assert create_res.status_code == 422

    print(f"create_repository() response: {create_res.status_code}")
