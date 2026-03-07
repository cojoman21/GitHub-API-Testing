from pydantic import TypeAdapter

from api_clients.repo_client import RepoClient
from models.base_model import RepositoryResponse


def test_repo_pagination(repo_client: RepoClient, multiple_repos):
    """Verify that pagination limits results and can navigate pages"""

    # Create an adapter that will validate the response using Pydantic
    adapter = TypeAdapter(list[RepositoryResponse])
    all_pages_data = []

    # Iterate through the first 3 pages to verify pagination logic
    for page_num in range(1, 4):
        # Fetch page and verify successful API response
        list_res = repo_client.list_repositories(page=page_num, per_page=1)
        assert list_res.status_code == 200

        # Validate response schema and page size
        data = adapter.validate_python(list_res.json())
        assert len(data) == 1, f"Page {page_num} should have exactly 1 item"

        # Store repo object for uniqueness check
        all_pages_data.append(data[0])

    # Extract IDs and use a set to ensure no overlapping data between pages
    ids = [repo.id for repo in all_pages_data]
    assert len(set(ids)) == 3, "Detected overlapping repositories across pages"
