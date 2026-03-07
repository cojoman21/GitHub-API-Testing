from api_clients.repo_client import RepoClient


def test_404_repo_not_found(repo_client: RepoClient):
    """Test GET on non-existent repository"""
    owner = repo_client.username
    get_res = repo_client.get_repository(owner, "fake_repo")

    assert get_res.status_code == 404

    print(f"get_repository() response: {get_res.status_code}")
