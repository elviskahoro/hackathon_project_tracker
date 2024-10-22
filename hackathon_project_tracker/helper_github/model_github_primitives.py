# trunk-ignore-all(trunk/ignore-does-nothing)
from __future__ import annotations

import datetime  # trunk-ignore(ruff/TCH003)
from typing import Any

from pydantic import Field

from hackathon_project_tracker.helper_universal_primitives import GitHubIssueStateType
from hackathon_project_tracker.helper_utils import GitHubIssueCode, GitHubIssueCodeTitle

from .pydantic_settings import BaseModel


class GitHubOrganization(BaseModel):
    avatar_url: str | None
    description: str | None
    events_url: str | None
    hooks_url: str | None
    id: int | None
    issues_url: str | None
    login: str | None
    members_url: str | None
    node_id: str | None
    public_members_url: str | None
    repos_url: str | None
    url: str | None


class GitHubReactions(BaseModel):
    plus_one: int | None = Field(
        alias="+1",
        default_factory=int,
    )
    minus_one: int | None = Field(
        alias="-1",
        default_factory=int,
    )
    confused: int | None
    eyes: int | None
    heart: int | None
    hooray: int | None
    laugh: int | None
    rocket: int | None
    total_count: int | None
    url: str | None


class GitHubLicense(BaseModel):
    key: str | None
    name: str | None
    node_id: str | None
    spdx_id: str | None
    url: Any | None


class GitHubRepositoryOwner(BaseModel):
    avatar_url: str | None
    events_url: str | None
    followers_url: str | None
    following_url: str | None
    gists_url: str | None
    gravatar_id: str | None
    html_url: str | None
    id: int | None
    login: str | None
    node_id: str | None
    organizations_url: str | None
    received_events_url: str | None
    repos_url: str | None
    site_admin: bool | None
    starred_url: str | None
    subscriptions_url: str | None
    type: str | None
    url: str | None


class GitHubRepository(BaseModel):
    allow_forking: bool | None
    archive_url: str | None
    archived: bool | None
    assignees_url: str | None
    blobs_url: str | None
    branches_url: str | None
    clone_url: str | None
    collaborators_url: str | None
    comments_url: str | None
    commits_url: str | None
    compare_url: str | None
    contents_url: str | None
    contributors_url: str | None
    created_at: datetime.datetime | None
    default_branch: str | None
    deployments_url: str | None
    description: str | None
    disabled: bool | None
    downloads_url: str | None
    events_url: str | None
    fork: bool | None
    forks: int | None
    forks_count: int | None
    forks_url: str | None
    full_name: str | None
    git_commits_url: str | None
    git_refs_url: str | None
    git_tags_url: str | None
    git_url: str | None
    has_downloads: bool | None
    has_issues: bool | None
    has_pages: bool | None
    has_projects: bool | None
    has_wiki: bool | None
    homepage: str | None
    hooks_url: str | None
    html_url: str | None
    id: int | None
    is_template: bool | None
    issue_comment_url: str | None
    issue_events_url: str | None
    issues_url: str | None
    keys_url: str | None
    labels_url: str | None
    language: Any | None
    languages_url: str | None
    license: GitHubLicense | None
    merges_url: str | None
    milestones_url: str | None
    mirror_url: Any | None
    name: str | None
    node_id: str | None
    notifications_url: str | None
    open_issues: int | None
    open_issues_count: int | None
    owner: GitHubRepositoryOwner | None
    private: bool | None
    pulls_url: str | None
    pushed_at: datetime.datetime | None
    releases_url: str | None
    size: int | None
    ssh_url: str | None
    stargazers_count: int | None
    stargazers_url: str | None
    statuses_url: str | None
    subscribers_url: str | None
    subscription_url: str | None
    svn_url: str | None
    tags_url: str | None
    teams_url: str | None
    topics: list[str] | None
    trees_url: str | None
    updated_at: datetime.datetime | None
    url: str | None
    visibility: str | None
    watchers: int | None
    watchers_count: int | None
    web_commit_signoff_required: bool | None

    def get_full_name(
        self: GitHubRepository,
    ) -> str:
        if github_full_name := self.full_name:
            return github_full_name

        raise AttributeError

    def get_name(
        self: GitHubRepository,
    ) -> str:
        if github_name := self.name:
            return github_name

        raise AttributeError


class GitHubUser(BaseModel):
    avatar_url: str | None
    events_url: str | None
    followers_url: str | None
    following_url: str | None
    gists_url: str | None
    gravatar_id: str | None
    html_url: str | None
    login: str | None
    node_id: str | None
    organizations_url: str | None
    received_events_url: str | None
    repos_url: str | None
    starred_url: str | None
    subscriptions_url: str | None
    type: str | None
    url: str | None
    id: int | None = None
    site_admin: bool | None = None

    def get_node_id(
        self: GitHubUser,
    ) -> str:
        if github_node_id := self.node_id:
            return github_node_id

        raise AttributeError

    def get_username(
        self: GitHubUser,
    ) -> str:
        if github_username := self.login:
            return github_username

        raise AttributeError

    def is_bot(
        self: GitHubUser,
    ) -> bool:
        match self.type:
            case "Bot":
                return True

            case "User":
                return False

            case "Organization":
                return False

            case _:
                raise ValueError

    def create_front_sender_handle(
        self: GitHubUser,
    ) -> str:
        if github_login := self.login:
            return f"GH-{github_login}"

        raise AttributeError

    def get_user(
        self: GitHubUser,
    ) -> str:
        if github_user := self.login:
            return github_user

        raise AttributeError


class GitHubFork(BaseModel):
    id: int | None
    node_id: str | None
    name: str | None
    full_name: str | None
    private: bool | None
    owner: GitHubUser | None
    html_url: str | None
    description: str | None
    fork: bool | None
    url: str | None
    forks_url: str | None
    keys_url: str | None
    collaborators_url: str | None
    teams_url: str | None
    hooks_url: str | None
    issue_events_url: str | None
    events_url: str | None
    assignees_url: str | None
    branches_url: str | None
    tags_url: str | None
    blobs_url: str | None
    git_tags_url: str | None
    git_refs_url: str | None
    trees_url: str | None
    statuses_url: str | None
    languages_url: str | None
    stargazers_url: str | None
    contributors_url: str | None
    subscribers_url: str | None
    subscription_url: str | None
    commits_url: str | None
    git_commits_url: str | None
    comments_url: str | None
    issue_comment_url: str | None
    contents_url: str | None
    compare_url: str | None
    merges_url: str | None
    archive_url: str | None
    downloads_url: str | None
    issues_url: str | None
    pulls_url: str | None
    milestones_url: str | None
    notifications_url: str | None
    labels_url: str | None
    releases_url: str | None
    deployments_url: str | None
    created_at: datetime.datetime | None
    updated_at: datetime.datetime | None
    pushed_at: datetime.datetime | None
    git_url: str | None
    ssh_url: str | None
    clone_url: str | None
    svn_url: str | None
    homepage: str | None
    size: int | None
    stargazers_count: int | None
    watchers_count: int | None
    has_issues: bool | None
    has_projects: bool | None
    has_downloads: bool | None
    has_wiki: bool | None
    has_pages: bool | None
    has_discussions: bool | None
    forks_count: int | None
    archived: bool | None
    disabled: bool | None
    open_issues_count: int | None
    license: GitHubLicense | None
    allow_forking: bool | None
    is_template: bool | None
    web_commit_signoff_required: bool | None
    topics: list[str] | None
    visibility: str | None
    forks: int | None
    open_issues: int | None
    watchers: int | None
    default_branch: str | None
    public: bool | None
    language: None
    mirror_url: None


class GitHubDiscussionCategory(BaseModel):
    id: int
    node_id: str
    repository_id: int
    emoji: str
    name: str
    description: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    slug: str
    is_answerable: bool


class GitHubDiscussion(BaseModel):
    repository_url: str
    category: GitHubDiscussionCategory
    answer_html_url: None
    answer_chosen_at: datetime.datetime
    answer_chosen_by: None
    html_url: str
    id: int
    node_id: str
    number: int
    title: str
    user: GitHubUser
    state: str
    state_reason: None
    locked: bool
    comments: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    author_association: str
    active_lock_reason: None
    body: str
    reactions: GitHubReactions
    timeline_url: str


class GitHubComment(BaseModel):
    user: GitHubUser
    performed_via_github_app: bool | None
    url: str | None = None
    html_url: str | None = None
    issue_url: str | None = None
    id: int | None = None
    node_id: str | None = None
    created_at: datetime.datetime | None = None
    updated_at: datetime.datetime | None = None
    author_association: str | None = None
    body: str | None = None
    reactions: GitHubReactions | None = None

    def get_body(
        self: GitHubComment,
    ) -> str:
        if github_body := self.body:
            return github_body

        raise AttributeError

    def get_created_at(
        self: GitHubComment,
    ) -> datetime.datetime:
        if github_created_at := self.created_at:
            return github_created_at

        raise AttributeError

    def get_node_id(
        self: GitHubComment,
    ) -> str:
        if github_node_id := self.node_id:
            return github_node_id

        raise AttributeError

    def get_url_html(
        self: GitHubComment,
    ) -> str:
        if github_url := self.html_url:
            return github_url

        raise AttributeError

    def get_user(
        self: GitHubComment,
    ) -> GitHubUser:
        if github_user := self.user:
            return github_user

        raise AttributeError

    def create_body_with_url(
        self: GitHubComment,
    ) -> str:
        github_url: str = self.get_url_html()
        github_body: str = self.get_body()
        github_body_with_url: str = f"{github_url}\n\n{github_body}"
        return github_body_with_url

    def is_from_bot(
        self: GitHubComment,
    ) -> bool:
        return self.user.is_bot()


class GitHubCommentChangesBody(BaseModel):
    body_from: str | None = None


class GitHubCommentChanges(BaseModel):
    body: GitHubCommentChangesBody | None = None


class GitHubLabel(BaseModel):
    id: int | None = None
    node_id: str | None = None
    url: str | None = None
    name: str | None = None
    color: str | None = None
    default: bool | None = None
    description: str | None = None

    def get_id(
        self: GitHubLabel,
    ) -> int:
        if github_label_id := self.id:
            return github_label_id

        raise AttributeError

    def get_name(
        self: GitHubLabel,
    ) -> str:
        if github_name := self.name:
            return github_name

        raise AttributeError

    def get_node_id(
        self: GitHubLabel,
    ) -> str:
        if github_node_id := self.node_id:
            return github_node_id

        raise AttributeError

    def is_bug(
        self: GitHubLabel,
    ) -> bool:
        github_name = self.get_name()
        return github_name == "Bug"


class GitHubIssue(BaseModel):
    active_lock_reason: Any | None
    assignee: GitHubUser | None
    assignees: list[GitHubUser] | None
    author_association: str | None
    body: str | None
    closed_at: datetime.datetime | None
    comments: int | None
    comments_url: str | None
    created_at: datetime.datetime | None
    events_url: str | None
    html_url: str | None
    id: int | None
    labels: list[GitHubLabel] | None
    labels_url: str | None
    locked: bool | None
    milestone: Any | None
    node_id: str | None
    number: int
    performed_via_github_app: Any | None
    reactions: GitHubReactions | None
    repository_url: str | None
    state: str | None
    state_reason: str | None
    timeline_url: str | None
    title: str | None
    updated_at: datetime.datetime | None
    url: str | None
    user: GitHubUser

    def get_body(
        self: GitHubIssue,
    ) -> str:
        if github_body := self.body:
            return github_body

        raise AttributeError

    def get_created_at(
        self: GitHubIssue,
    ) -> datetime.datetime:
        if github_created_at := self.created_at:
            return github_created_at

        raise AttributeError

    def get_github_issue_code(
        self: GitHubIssue,
    ) -> GitHubIssueCode:
        if self.number:
            return GitHubIssueCode.from_int(
                github_issue_number=self.number,
            )

        raise AttributeError

    def get_labels(
        self: GitHubIssue,
    ) -> list[GitHubLabel]:
        if github_labels := self.labels:
            return github_labels

        raise AttributeError

    def get_node_id(
        self: GitHubIssue,
    ) -> str:
        if github_node_id := self.node_id:
            return github_node_id

        raise AttributeError

    def get_github_state(
        self: GitHubIssue,
    ) -> GitHubIssueStateType:
        if github_state := self.state:
            return GitHubIssueStateType(github_state)

        raise AttributeError

    def get_state_reason(
        self: GitHubIssue,
    ) -> str:
        if github_state_reason := self.state_reason:
            return github_state_reason

        raise AttributeError

    def get_title(
        self: GitHubIssue,
    ) -> str:
        if github_title := self.title:
            return github_title

        raise AttributeError

    def get_url_html(
        self: GitHubIssue,
    ) -> str:
        if github_url := self.html_url:
            return github_url

        raise AttributeError

    def get_user(
        self: GitHubIssue,
    ) -> GitHubUser:
        if github_user := self.user:
            return github_user

        raise AttributeError

    def create_body_with_url(
        self: GitHubIssue,
    ) -> str:
        github_url: str = self.get_url_html()
        github_body: str = self.get_body()
        github_body_with_url: str = f"{github_url}\n\n{github_body}"
        return github_body_with_url

    def get_github_issue_code_title(
        self: GitHubIssue,
    ) -> GitHubIssueCodeTitle:
        title: str = self.get_title()
        github_issue_code: GitHubIssueCode = self.get_github_issue_code()
        return GitHubIssueCodeTitle.from_title_and_github_issue_code(
            title=title,
            github_issue_code=github_issue_code,
        )

    def is_from_bot(
        self: GitHubIssue,
    ) -> bool:
        return self.user.is_bot()
