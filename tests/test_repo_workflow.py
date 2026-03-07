import uuid

from api_clients.repo_client import RepoClient
from models.base_model import RepositoryResponse


def test_repo_workflow(repo_client: RepoClient, request):
    """Test the CRUD workflow for a GitHub repository"""

    current_name = f"repo-{uuid.uuid4().hex[:6]}"
    new_name = f"repo-{uuid.uuid4().hex[:6]}"
    # GitHub token
    owner = repo_client.username

    # 1. Create/POST the repo
    create_res = repo_client.create_repository(current_name)

    # To make sure the repo gets deleted even if the test fails
    request.addfinalizer(lambda: repo_client.delete_with_retry(owner, current_name))

    assert create_res.status_code == 201

    # Validate the API response using pydantic
    create_res_data = RepositoryResponse.model_validate(create_res.json())

    assert create_res_data.name == current_name

    # 2. Read/GET the repo
    get_res = repo_client.get_repository(owner, repo=current_name)
    assert get_res.status_code == 200

    get_res_data = RepositoryResponse.model_validate(get_res.json())

    assert get_res_data.name == current_name

    ## 3. Update/PATCH the repo
    update_res = repo_client.update_with_retry(
        owner, repo=current_name, new_name=new_name
    )

    # To make sure our addfinalizer will delete the correct repo, if the name change was successful
    current_name = new_name

    update_res_data = RepositoryResponse.model_validate(update_res.json())

    assert update_res_data.name == new_name

    # Read/GET again with the new repo name
    get_res = repo_client.get_repository(owner, repo=new_name)
    assert get_res.status_code == 200

    get_res_data = RepositoryResponse.model_validate(get_res.json())

    assert get_res_data.name == new_name
