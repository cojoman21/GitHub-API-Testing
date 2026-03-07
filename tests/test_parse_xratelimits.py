from api_clients.repo_client import RepoClient
from models.base_model import RateLimitResponse


def test_parse_xratelimits(repo_client: RepoClient, temp_repo):
    """Test: read the X-RateLimit headers"""
    repo_name = temp_repo
    owner = repo_client.username

    get_res = repo_client.get_repository(owner, repo_name)

    headers_lower = {k.lower(): v for k, v in get_res.headers.items()}
    get_res_data = RateLimitResponse.model_validate(headers_lower)

    limit = get_res.headers.get("X-RateLimit-Limit")
    remaining = get_res.headers.get("X-RateLimit-Remaining")
    reset_time = get_res.headers.get("X-RateLimit-Reset")

    print(get_res_data)

    assert limit is not None
    assert int(remaining) >= 0
    assert int(reset_time) > 0
