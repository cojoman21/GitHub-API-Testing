import time

from .base_client import GitHubClient


class RepoClient(GitHubClient):
    # name = the repo name
    # description = repo description
    def create_repository(self, name: str, description: str = ""):
        payload = {"name": name, "description": description, "auto_init": True}
        return self.session.post(f"{self.base_url}/user/repos", json=payload)

    def create_repository_without_name(self, description: str = ""):
        payload = {"description": description, "auto_init": True}
        return self.session.post(f"{self.base_url}/user/repos", json=payload)

    def get_repository(self, owner: str, repo: str):
        return self.session.get(f"{self.base_url}/repos/{owner}/{repo}")

    def update_repository(self, owner, repo, new_name: str, new_description: str = ""):
        payload = {"name": new_name, "description": new_description}
        return self.session.patch(f"{self.base_url}/repos/{owner}/{repo}", json=payload)

    def list_repositories(
        self,
        page: int = 1,
        per_page: int = 30,
        sort: str = "created",
        direction: str = "asc",
    ):
        """
        List repositories with explicit sorting to ensure pagination stability.
        - sort: created, updated, pushed, full_name
        - direction: asc, desc
        """
        params = {
            "page": page,
            "per_page": per_page,
            "sort": sort,
            "direction": direction,
        }
        return self.session.get(f"{self.base_url}/user/repos", params=params)

    def delete_repository(self, owner: str, repo: str):
        return self.session.delete(f"{self.base_url}/repos/{owner}/{repo}")

    # Delete with retry to avoid moving too fast for GitHub
    def delete_with_retry(self, owner, repo: str, retries=3):
        for i in range(retries):
            delete_res = self.delete_repository(owner, repo)
            if delete_res.status_code == 204:
                return delete_res
            if delete_res.status_code == 409:
                time.sleep(2)
            else:
                raise RuntimeError(
                    f"Unexpected error {delete_res.status_code}: {delete_res.text}"
                )

        raise TimeoutError(
            f"GitHub was too busy to delete {repo} after {retries} attempts."
        )

    # Update with retry to avoid moving too fast for GitHub
    def update_with_retry(self, owner, repo, new_name: str, retries=3):
        for i in range(retries):
            update_res = self.update_repository(owner, repo, new_name=new_name)
            if update_res.status_code == 200:
                return update_res
            if update_res.status_code == 422:
                time.sleep(2)
            else:
                raise RuntimeError(
                    f"Unexpected error {update_res.status_code}: {update_res.status_code}"
                )

        raise TimeoutError(
            f"GitHub was too busy to update {repo} after {retries} attempts."
        )
