import os

import requests
from dotenv import load_dotenv

load_dotenv()


class GitHubClient:
    def __init__(self, token=None):
        self.base_url = "https://api.github.com"
        self.session = requests.Session()
        # auth_token allows us to pass a custom token (for example when we're doing the wrong token test)
        self.auth_token = token or os.getenv("AUTH_TOKEN")
        # the accept and the authorization headers that are required by GitHub
        self.session.headers.update(
            {
                "Authorization": f"Bearer {self.auth_token}",
                "Accept": "application/vnd.github+json",
            }
        )
        self.username: str = os.getenv("AUTH_USER")
