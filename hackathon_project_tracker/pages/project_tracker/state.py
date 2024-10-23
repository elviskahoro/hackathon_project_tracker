from __future__ import annotations

import os

import reflex as rx
from github import Github

from hackathon_project_tracker import helper_github
from hackathon_project_tracker.helper_github.model_github_primitives import GitHubIssue

TOKENS: dict[str, str] = {
    "GITHUB_OWNER": "reflex-dev",
    "GITHUB_REPO": "reflex",
    "GITHUB_CLIENT_ID": os.getenv("GITHUB_CLIENT_ID"),
    "GITHUB_CLIENT_SECRET": os.getenv("GITHUB_CLIENT_SECRET"),
}

GITHUB_CLIENT: Github = helper_github.set_up_client_from_tokens(
    tokens=TOKENS,
)
GITHUB_REPO_PATH_DEFAULT: str = helper_github.create_repo_path(
    tokens=TOKENS,
)


class State(rx.State):
    """The state for the project tracker page."""

    title: str = "Hackathon Project Tracker"
    current_repo_path: str = GITHUB_REPO_PATH_DEFAULT

    repo_table: list[GitHubIssue] = []

    def on_load(
        self: State,
    ) -> None:
        pass
        # repo: Repository = GITHUB_CLIENT.get_repo(
        #     full_name_or_id=GITHUB_REPO_PATH_DEFAULT,
        # )
        # pulls: PaginatedList[PullRequest] = repo.get_pulls()
        # pull: PullRequest
        # for pull in pulls:
        #     print(pull._rawData)

    def placeholder_function(
        self: State,
    ) -> None:
        pass
