from api_clients.repo_client import RepoClient


def test_401_invalid_token(unauthorized_repo_client: RepoClient):
    """Test creating repository with bad token"""
    create_res = unauthorized_repo_client.create_repository("test-repo")
    assert create_res.status_code == 401

    print(f"create_repository() response: {create_res.status_code}")
