from api_clients.repo_client import RepoClient


def test_422_create_repo_without_name(repo_client: RepoClient):
    """Test creating a repository without a name"""
    create_res = repo_client.create_repository_without_name()

    assert create_res.status_code == 422

    print(f"create_repository_without_name() response: {create_res.status_code}")
