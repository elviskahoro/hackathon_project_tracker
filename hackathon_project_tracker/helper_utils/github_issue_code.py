# trunk-ignore-all(trunk/ignore-does-nothing)
from __future__ import annotations

import re
from re import Match, Pattern

from pydantic import BaseModel, RootModel, field_validator

from hackathon_project_tracker.helper_logging import Severity, log

DEFAULT_GITHUB_URL_BASE: str = "https://github.com"
DEFAULT_GITHUB_ORG: str = "reflex-dev"
DEFAULT_GITHUB_REPO: str = "reflex"

REGEX_GITHUB_ISSUE_CODE: str = r"GH\d+"


class GitHubUrlBase(BaseModel):
    url: str = DEFAULT_GITHUB_URL_BASE

    def __str__(
        self: GitHubUrlBase,
    ) -> str:
        return self.url


class GitHubUrlOrg(GitHubUrlBase):
    org: str = DEFAULT_GITHUB_ORG

    def __str__(
        self: GitHubUrlOrg,
    ) -> str:
        return self.url

    @classmethod
    def from_string_org(
        cls: type[GitHubUrlOrg],
        org: str = DEFAULT_GITHUB_ORG,
    ) -> GitHubUrlOrg:
        github_url_base: GitHubUrlBase = GitHubUrlBase()
        url: str = f"{github_url_base!s}/{org}"
        return GitHubUrlOrg(
            url=url,
            org=org,
        )


class GitHubUrlRepo(GitHubUrlOrg):
    repo: str = DEFAULT_GITHUB_REPO

    def __str__(
        self: GitHubUrlRepo,
    ) -> str:
        return self.url

    @classmethod
    def from_string_repo(
        cls: type[GitHubUrlRepo],
        org: str = DEFAULT_GITHUB_ORG,
        repo: str = DEFAULT_GITHUB_REPO,
    ) -> GitHubUrlRepo:
        github_url_org: GitHubUrlOrg = GitHubUrlOrg.from_string_org(
            org=org,
        )
        url: str = f"{github_url_org!s}/{repo}"
        return GitHubUrlRepo(
            url=url,
            repo=repo,
            org=github_url_org.org,
        )


class GitHubUrlIssue(GitHubUrlRepo):
    issue_number: int

    def __str__(
        self: GitHubUrlIssue,
    ) -> str:
        return self.url

    @staticmethod
    def get_url(
        org: str = DEFAULT_GITHUB_ORG,
        repo: str = DEFAULT_GITHUB_REPO,
    ) -> str:
        url_repo: str = str(
            GitHubUrlRepo.from_string_repo(
                org=org,
                repo=repo,
            ),
        )
        return f"{url_repo}/issues"

    @classmethod
    def from_string_issue(
        cls: type[GitHubUrlIssue],
        github_issue_number: int,
        org: str = DEFAULT_GITHUB_ORG,
        repo: str = DEFAULT_GITHUB_REPO,
    ) -> GitHubUrlIssue:
        github_url_repo: GitHubUrlRepo = GitHubUrlRepo.from_string_repo(
            org=org,
            repo=repo,
        )
        url_repo: str = GitHubUrlIssue.get_url(
            org=github_url_repo.org,
            repo=github_url_repo.repo,
        )
        url: str = f"{url_repo}/{github_issue_number}"
        return GitHubUrlIssue(
            url=url,
            issue_number=github_issue_number,
            org=github_url_repo.org,
            repo=github_url_repo.repo,
        )


class GitHubIssueCode(RootModel):
    root: str

    def __eq__(
        self: GitHubIssueCode,
        __value: object,
    ) -> bool:
        return self.root == __value.root  # type: ignore

    def __str__(
        self: GitHubIssueCode,
    ) -> str:
        return self.root

    @staticmethod
    def _check_github_issue_code_string(
        github_issue_code: str,
    ) -> bool:
        return bool(
            re.fullmatch(
                pattern=REGEX_GITHUB_ISSUE_CODE,
                string=github_issue_code,
            ),
        )

    @classmethod
    def from_string_exact(
        cls: type[GitHubIssueCode],
        github_issue_code_raw: str,
    ) -> GitHubIssueCode:
        if GitHubIssueCode._check_github_issue_code_string(
            github_issue_code=github_issue_code_raw,
        ):
            return GitHubIssueCode(
                root=github_issue_code_raw,
            )

        raise ValueError

    @classmethod
    def from_string(
        cls: type[GitHubIssueCode],
        string_with_github_issue_code: str,
    ) -> GitHubIssueCode:
        github_issue_code_candidates = re.findall(
            pattern=REGEX_GITHUB_ISSUE_CODE,
            string=string_with_github_issue_code,
        )
        number_of_candidates: int = len(github_issue_code_candidates)
        if number_of_candidates > 1:
            log(
                the_log=f"Multiple GH issue number candidates found in: {string_with_github_issue_code}",
                severity=Severity.ERROR,
                file=__file__,
            )
            raise ValueError

        if number_of_candidates == 0:
            raise AttributeError

        github_issue_code_raw, *_ = github_issue_code_candidates
        return GitHubIssueCode.from_string_exact(
            github_issue_code_raw=github_issue_code_raw,
        )

    @classmethod
    def from_int(
        cls: type[GitHubIssueCode],
        github_issue_number: int,
    ) -> GitHubIssueCode:
        """Formats an issue number and returns a cleaned version.  24 -> 024."""
        github_issue_code_raw: str = f"GH{github_issue_number:05d}"
        return GitHubIssueCode.from_string_exact(
            github_issue_code_raw=github_issue_code_raw,
        )

    @classmethod
    def from_github_issue_url(
        cls: type[GitHubIssueCode],
        github_url_issue: str,
    ) -> GitHubIssueCode:
        re_github_issue_number: str = r"(\d{3,5})"
        re_github_issue_number_pattern: Pattern = re.compile(
            re_github_issue_number,
        )
        re_match: Match | None = re.search(
            re_github_issue_number_pattern,
            github_url_issue,
        )
        if re_match is None:
            raise AssertionError

        match_digits_first: str = re_match[0]
        github_issue_number: int = int(match_digits_first)
        return GitHubIssueCode.from_int(
            github_issue_number=github_issue_number,
        )

    @field_validator("root")  # trunk-ignore(mypy/misc)
    @classmethod
    def validate_github_issue_code(
        cls: type[GitHubIssueCode],  # trunk-ignore(ruff/N805)
        v: object,  # trunk-ignore(pylint/C0103)
    ) -> object:
        match v:

            case str():
                if GitHubIssueCode._check_github_issue_code_string(
                    github_issue_code=v,
                ):
                    return v

                raise ValueError

            case _:
                raise TypeError

    def get_github_issue_number(
        self: GitHubIssueCode,
    ) -> int:
        matches: list[re.Match] = re.findall(
            pattern=r"\d+",
            string=self.root,
        )
        list_of_digits: list[int] = list(
            map(
                int,  # type: ignore
                matches,
            ),
        )
        match len(list_of_digits):

            case 0:
                log(
                    the_log="No matches found",
                    severity=Severity.ERROR,
                    file=__file__,
                )
                raise ValueError

            case 1:
                return list_of_digits[0]

            case _:
                log(
                    the_log="Multiple matches found, there should be only a single match",
                    severity=Severity.ERROR,
                    file=__file__,
                )
                raise ValueError

    def create_url(
        self: GitHubIssueCode,
        org: str = DEFAULT_GITHUB_ORG,
        repo: str = DEFAULT_GITHUB_REPO,
    ) -> str:
        return str(
            GitHubUrlIssue.from_string_issue(
                github_issue_number=self.get_github_issue_number(),
                org=org,
                repo=repo,
            ),
        )


class GitHubIssueCodeTitle(BaseModel):
    github_issue_code_title: str
    github_issue_code: GitHubIssueCode

    def __eq__(
        self: GitHubIssueCodeTitle,
        __value: object,
    ) -> bool:
        return self.github_issue_code_title == __value.github_issue_code_title  # type: ignore

    def __str__(
        self: GitHubIssueCodeTitle,
    ) -> str:
        return self.github_issue_code_title

    def validate_integrity(
        self: GitHubIssueCodeTitle,
    ) -> bool:
        github_issue_code_title: str = self.github_issue_code_title
        github_issue_code_for_title: GitHubIssueCode = GitHubIssueCode.from_string(
            string_with_github_issue_code=github_issue_code_title,
        )
        return github_issue_code_for_title == self.github_issue_code

    @classmethod
    def from_title_and_github_issue_code(
        cls: type[GitHubIssueCodeTitle],
        title: str,
        github_issue_code: GitHubIssueCode,
    ) -> GitHubIssueCodeTitle:
        github_issue_code_title: str = f"{github_issue_code!s} - {title}"
        return GitHubIssueCodeTitle(
            github_issue_code=github_issue_code,
            github_issue_code_title=github_issue_code_title,
        )
