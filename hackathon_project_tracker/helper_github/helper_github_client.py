from __future__ import annotations

from github import Github

from hackathon_project_tracker import helper_utils
from hackathon_project_tracker.helper_logging import Severity, log


def create_repo_path(
    tokens: (
        dict[
            str,
            str | None,
        ]
        | None
    ),
) -> str:
    tokens = helper_utils.check_tokens(
        tokens=tokens,
    )
    github_owner: str | None = tokens.get(
        "GITHUB_OWNER",
        None,
    )
    github_repo: str | None = tokens.get(
        "GITHUB_REPO",
        None,
    )
    if github_owner is None:
        raise AttributeError

    if github_repo is None:
        raise AttributeError

    github_repo_path: str = f"{github_owner}/{github_repo}"
    match len(github_repo_path):

        case 0 | 1:
            raise AttributeError

        case _:
            return github_repo_path


def set_up_client_from_tokens(
    tokens: (
        dict[
            str,
            str | None,
        ]
        | None
    ),
) -> Github:
    tokens = helper_utils.check_tokens(
        tokens=tokens,
    )
    log(
        the_log="Setting up client",
        severity=Severity.DEBUG,
        file=__file__,
    )
    github_owner: str | None = tokens.get(
        "GITHUB_OWNER",
        None,
    )
    if github_owner is None:
        raise AttributeError("GITHUB_OWNER is not set")

    github_repo: str | None = tokens.get(
        "GITHUB_REPO",
        None,
    )
    if github_repo is None:
        raise AttributeError("GITHUB_REPO is not set")


    github_client_id: str | None = tokens.get(
        "GITHUB_CLIENT_ID",
        None,
    )
    if github_client_id is None:
        raise AttributeError("GITHUB_CLIENT_ID is not set")

    github_client_secret: str | None = tokens.get(
        "GITHUB_CLIENT_SECRET",
        None,
    )
    if github_client_secret is None:
        raise AttributeError("GITHUB_CLIENT_SECRET is not set")

    github_client: Github = Github()
    github_client.get_oauth_application(
        client_id=github_client_id,
        client_secret=github_client_secret,
    )
    return github_client
