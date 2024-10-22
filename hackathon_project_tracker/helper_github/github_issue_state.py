from __future__ import annotations

from enum import Enum, auto


class GitHubIssueStateType(Enum):
    CLOSED = "closed"
    OPENED = "opened"


class GitHubIssueStateReasonType(Enum):
    COMPLETED = auto()
    NOT_PLANNED = auto()

    @classmethod
    def from_github_issue_state_reason(
        cls: type[GitHubIssueStateReasonType],
        github_issue_state_reason: str,
    ) -> GitHubIssueStateReasonType:
        match github_issue_state_reason:

            case "completed":
                return GitHubIssueStateReasonType.COMPLETED

            case "not_planned":
                return GitHubIssueStateReasonType.NOT_PLANNED

            case "reopened":
                return GitHubIssueStateReasonType.COMPLETED

            case _:
                error_msg: str = (
                    f"GitHub: Issue State Reason Type: Null: {github_issue_state_reason}"
                )
                raise ValueError(
                    error_msg,
                )
