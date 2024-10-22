# trunk-ignore-all(ruff/TCH001)
from __future__ import annotations

import datetime  # trunk-ignore(ruff/TCH003)

from hackathon_project_tracker.helper_logging import Severity, log

from .model_github_primitives import (
    GitHubComment,
    GitHubCommentChanges,
    GitHubDiscussion,
    GitHubFork,
    GitHubIssue,
    GitHubLabel,
    GitHubOrganization,
    GitHubRepository,
    GitHubUser,
)
from .pydantic_settings import BaseModel


class GitHubPayloadFork(BaseModel):
    forkee: GitHubFork
    repository: GitHubRepository
    organization: GitHubOrganization
    sender: GitHubUser

    def validate_response(
        self: GitHubPayloadFork,
    ) -> None:
        log(
            the_log=f"Successfully parsed the payload with: {self.__class__.__name__}",
            severity=Severity.DEBUG,
            file=__file__,
        )


class GitHubPayloadCommentCreated(BaseModel):
    action: str
    issue: GitHubIssue
    repository: GitHubRepository
    organization: GitHubOrganization
    sender: GitHubUser
    comment: GitHubComment

    def get_github_comment(
        self: GitHubPayloadCommentCreated,
    ) -> GitHubComment:
        if github_comment := self.comment:
            return github_comment

        raise AttributeError

    def get_github_issue(
        self: GitHubPayloadCommentCreated,
    ) -> GitHubIssue:
        if github_issue := self.issue:
            return github_issue

        raise AttributeError

    def get_github_user(
        self: GitHubPayloadCommentCreated,
    ) -> GitHubUser:
        if github_user := self.sender:
            return github_user

        raise AttributeError


class GitHubPayloadDiscussionCommentEdited(BaseModel):
    action: str
    changes: GitHubCommentChanges
    repository: GitHubRepository
    organization: GitHubOrganization
    sender: GitHubUser
    comment: GitHubComment
    discussion: GitHubDiscussion

    def get_github_issue(
        self: GitHubPayloadDiscussionCommentEdited,
    ) -> GitHubIssue:
        raise TypeError


class GitHubPayloadIssueCommentEdited(BaseModel):
    action: str
    changes: GitHubCommentChanges
    issue: GitHubIssue
    repository: GitHubRepository
    organization: GitHubOrganization
    sender: GitHubUser
    comment: GitHubComment

    def get_github_issue(
        self: GitHubPayloadIssueCommentEdited,
    ) -> GitHubIssue:
        if github_issue := self.issue:
            return github_issue

        raise AttributeError


class GitHubPayloadIssueClosed(BaseModel):
    action: str
    issue: GitHubIssue
    repository: GitHubRepository
    organization: GitHubOrganization
    sender: GitHubUser

    def get_github_issue(
        self: GitHubPayloadIssueClosed,
    ) -> GitHubIssue:
        if github_issue := self.issue:
            return github_issue

        raise AttributeError


class GitHubPayloadIssueLabeled(BaseModel):
    action: str
    issue: GitHubIssue
    label: GitHubLabel
    repository: GitHubRepository
    organization: GitHubOrganization
    sender: GitHubUser

    def get_github_issue(
        self: GitHubPayloadIssueLabeled,
    ) -> GitHubIssue:
        if github_issue := self.issue:
            return github_issue

        raise AttributeError


class GitHubPayloadIssueUnlabeled(BaseModel):
    action: str
    issue: GitHubIssue
    label: GitHubLabel
    repository: GitHubRepository
    organization: GitHubOrganization
    sender: GitHubUser

    def get_github_issue(
        self: GitHubPayloadIssueUnlabeled,
    ) -> GitHubIssue:
        if github_issue := self.issue:
            return github_issue

        raise AttributeError


class GitHubPayloadIssueOpen(BaseModel):
    action: str
    issue: GitHubIssue
    repository: GitHubRepository
    organization: GitHubOrganization
    sender: GitHubUser

    def get_github_issue(
        self: GitHubPayloadIssueOpen,
    ) -> GitHubIssue:
        raise TypeError

    def validate(
        self: GitHubPayloadIssueOpen,
    ) -> bool:
        return self.action == "opened"


class GitHubPayloadStarred(BaseModel):
    action: str
    repository: GitHubRepository
    organization: GitHubOrganization
    sender: GitHubUser

    starred_at: datetime.datetime | None = None
