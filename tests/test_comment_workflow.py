from api_clients.comment_client import CommentClient
from api_clients.repo_client import RepoClient


def test_comment_workflow(
    repo_client: RepoClient,
    temp_repo_name: str,
    temp_issue_number: int,
    comment_client: CommentClient,
):
    """Test the CRUD workflow for a GitHub comment on an repository issue"""
    # temp_repo_name uses the temp_repo fixture to create the repo and yield the name as str
    # temp_issue_number uses the temp_issue fixture to create the issue and yield the issue number as int
    repo_name = temp_repo_name
    issue_number = temp_issue_number
    # GitHub token
    owner = repo_client.username

    # Create/POST comment and check if the operation was successful
    create_res = comment_client.create_comment(owner, repo_name, issue_number)

    assert create_res.status_code == 201

    print(f"create_comment() response: {create_res.status_code}")

    # Extract the comment_id and check if create was successful
    comment_id = create_res.json()["id"]

    # Read/GET the comment and check if the operation was successful
    get_res = comment_client.get_comment(owner, repo_name, comment_id)
    assert get_res.status_code == 200

    print(f"get_comment() response: {get_res.status_code}")

    assert get_res.json()["body"] == "Reproduced on the latest build"

    # List/GET comments and check if the operation was successful
    list_res = comment_client.list_comments(owner, repo_name, issue_number)
    assert list_res.status_code == 200

    print(f"list_comments() response: {list_res.status_code}")

    comments_data = list_res.json()
    # assert "body" in comments_data
    if comments_data:
        assert "body" in comments_data[0]

    # Print the comments in format User | Comment
    for c in comments_data:
        print(f"User: {c['user']['login']} | Comment: {c['body']}")

    # Update/PATCH the comment and check if successful
    update_res = comment_client.update_comment(owner, repo_name, comment_id)
    assert update_res.status_code == 200

    print(f"update_comment() response: {update_res.status_code}")

    assert update_res.json()["body"] == "Updated comment"

    # List/GET the updated comment
    list_res = comment_client.list_comments(owner, repo_name, issue_number)
    # and check if it was successful
    assert list_res.status_code == 200

    print(f"list_comments() response: {list_res.status_code}")

    comments_data = list_res.json()
    # assert "body" in comments_data
    if comments_data:
        assert "body" in comments_data[0]
    # Print the updated comment
    for c in comments_data:
        print(f"User: {c['user']['login']} | Comment: {c['body']}")

    # DELETE comment and assert if the operation was successful
    delete_res = comment_client.delete_comment(owner, repo_name, comment_id)
    # Check if delete was successful
    assert delete_res.status_code == 204

    print(f"delete_comment() response: {delete_res.status_code}")


# The issue and the repo go out of scope and get automatically deleted here
