from api_clients.base_client import GitHubClient


class CommentClient(GitHubClient):
    def create_comment(
        self,
        owner: str,
        repo: str,
        issue_number: int,
        body: str = "Reproduced on the latest build",
    ):
        return self.session.post(
            f"{self.base_url}/repos/{owner}/{repo}/issues/{issue_number}/comments",
            json={"body": body},
        )

    def get_comment(self, owner: str, repo: str, comment_id: int):
        return self.session.get(
            f"{self.base_url}/repos/{owner}/{repo}/issues/comments/{comment_id}"
        )

    def update_comment(
        self,
        owner: str,
        repo: str,
        comment_id: int,
        body: str = "Updated comment",
    ):
        return self.session.patch(
            f"{self.base_url}/repos/{owner}/{repo}/issues/comments/{comment_id}",
            json={"body": body},
        )

    def list_comments(self, owner: str, repo: str, issue_number: int):
        return self.session.get(
            f"{self.base_url}/repos/{owner}/{repo}/issues/{issue_number}/comments"
        )

    def delete_comment(self, owner: str, repo: str, comment_id: int):
        return self.session.delete(
            f"{self.base_url}/repos/{owner}/{repo}/issues/comments/{comment_id}"
        )
