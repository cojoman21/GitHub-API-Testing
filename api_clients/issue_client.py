from .base_client import GitHubClient


class IssueClient(GitHubClient):
    def create_issue(self, owner: str, repo: str, title: str, body: str = ""):
        payload = {
            "title": title,
            "body": body,
        }
        return self.session.post(
            f"{self.base_url}/repos/{owner}/{repo}/issues", json=payload
        )

    def get_issue(self, owner: str, repo: str, issue_number: int):
        return self.session.get(
            f"{self.base_url}/repos/{owner}/{repo}/issues/{issue_number}"
        )

    def update_issue(
        self, owner: str, repo: str, issue_number: int, new_title: str = "New Title"
    ):
        return self.session.patch(
            f"{self.base_url}/repos/{owner}/{repo}/issues/{issue_number}",
            json={"title": new_title},
        )

    def delete_issue(
        self, owner: str, repo: str, issue_number: int, state: str = "closed"
    ):
        return self.session.patch(
            f"{self.base_url}/repos/{owner}/{repo}/issues/{issue_number}",
            json={"state": state},
        )
