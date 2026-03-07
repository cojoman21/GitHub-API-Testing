from unittest.mock import MagicMock, patch

from api_clients.repo_client import RepoClient
from models.base_model import RateLimitResponse


def test_mock_xratelimit_limit_reached(repo_client: RepoClient, limit_reached_data):
    """Simulate GitHub X-RateLimit-Limit being reached"""
    mock_response = MagicMock()
    mock_response.headers = limit_reached_data

    with patch.object(repo_client, "get_repository", return_value=mock_response):
        headers_lower = {k.lower(): v for k, v in mock_response.headers.items()}

        rate_limit_data = RateLimitResponse.model_validate(headers_lower)

        assert rate_limit_data.remaining == 0
        assert rate_limit_data.limit == 60
        assert rate_limit_data.used == 60
