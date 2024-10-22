# trunk-ignore-all(trunk/ignore-does-nothing)
from __future__ import annotations

import datetime  # trunk-ignore(ruff/TCH003)
from enum import Enum

from .model_github_primitives import (
    GitHubOrganization,  # trunk-ignore(ruff/TCH001)
    GitHubRepository,  # trunk-ignore(ruff/TCH001)
    GitHubUser,  # trunk-ignore(ruff/TCH001)
)
from .pydantic_settings import BaseModel


class GitHubPackage(BaseModel):
    ecosystem: str | None
    name: str | None


class GitHubAlertSecurityAdvisorySeverity(Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class GitHubAlertSecurityAdvisoryCvss(BaseModel):
    vector_string: str | None
    score: float | None


class GitHubAlertSecurityAdvisoryCwe(BaseModel):
    cwe_id: str | None
    name: str | None


class GitHubAlertSecurityAdvisoryIdentifier(BaseModel):
    value: str | None
    type: str | None


class GitHubAlertSecurityAdvisoryReference(BaseModel):
    url: str | None


class GitHubVulnerabilityFirstPatchedVersion(BaseModel):
    identifier: str | None


class GitHubVulnerability(BaseModel):
    package: GitHubPackage | None
    severity: str | None
    vulnerable_version_range: str | None
    first_patched_version: GitHubVulnerabilityFirstPatchedVersion | None


class GitHubAlertSecurityAdvisory(BaseModel):
    ghsa_id: str | None
    cve_id: str | None
    summary: str | None
    description: str | None
    severity: str | None
    identifiers: list[GitHubAlertSecurityAdvisoryIdentifier] | None
    references: list[GitHubAlertSecurityAdvisoryReference] | None
    published_at: datetime.datetime | None
    updated_at: datetime.datetime | None
    withdrawn_at: None
    vulnerabilities: list[GitHubVulnerability] | None
    cvss: GitHubAlertSecurityAdvisoryCvss | None
    cwes: list[GitHubAlertSecurityAdvisoryCwe] | None

    def get_description(
        self: GitHubAlertSecurityAdvisory,
    ) -> str:
        if github_description := self.description:
            return github_description

        raise AttributeError

    def get_ghsa_id(
        self: GitHubAlertSecurityAdvisory,
    ) -> str:
        if github_ghsa_id := self.ghsa_id:
            return github_ghsa_id

        raise AttributeError

    def get_summary(
        self: GitHubAlertSecurityAdvisory,
    ) -> str:
        if github_summary := self.summary:
            return github_summary

        raise AttributeError

    def get_severity(
        self: GitHubAlertSecurityAdvisory,
    ) -> str:
        if github_severity := self.severity:
            return github_severity

        raise AttributeError


class GitHubAlertDependency(BaseModel):
    package: GitHubPackage | None
    manifest_path: str | None
    scope: str | None


class GitHubAlert(BaseModel):
    number: int | None
    state: str | None
    created_at: datetime.datetime | None
    dismissed_comment: None = None
    dependency: GitHubAlertDependency | None = None
    security_advisory: GitHubAlertSecurityAdvisory | None = None
    security_vulnerability: GitHubVulnerability | None = None
    url: str | None = None
    html_url: str | None = None
    updated_at: datetime.datetime | None = None
    dismissed_at: datetime.datetime | None = None
    dismissed_by: str | None = None
    dismissed_reason: str | None = None
    fixed_at: datetime.datetime | None = None
    auto_dismissed_at: datetime.datetime | None = None
    id: int | None = None
    node_id: str | None = None
    affected_range: str | None = None
    affected_package_name: str | None = None
    external_reference: str | None = None
    external_identifier: str | None = None
    ghsa_id: str | None = None
    severity: str | None = None
    fixed_in: str | None = None

    def get_external_reference(
        self: GitHubAlert,
    ) -> str:
        if external_reference := self.external_reference:
            return external_reference

        raise AttributeError

    def get_ghsa_id(
        self: GitHubAlert,
    ) -> str:
        if github_ghsa_id := self.ghsa_id:
            return github_ghsa_id

        raise AttributeError

    def get_html_url(
        self: GitHubAlert,
    ) -> str:
        if github_html_url := self.html_url:
            return github_html_url

        raise AttributeError

    def get_security_advisory(
        self: GitHubAlert,
    ) -> GitHubAlertSecurityAdvisory:
        if github_security_advisory := self.security_advisory:
            return github_security_advisory

        raise AttributeError


class GitHubPayloadAlert(BaseModel):
    action: str | None
    alert: GitHubAlert | None
    repository: GitHubRepository | None
    organization: GitHubOrganization | None
    sender: GitHubUser | None

    def get_action(
        self: GitHubPayloadAlert,
    ) -> str:
        if github_action := self.action:
            return github_action

        raise AttributeError

    def get_alert(
        self: GitHubPayloadAlert,
    ) -> GitHubAlert:
        if github_alert := self.alert:
            return github_alert

        raise AttributeError

    def get_repository(
        self: GitHubPayloadAlert,
    ) -> GitHubRepository:
        if github_repository := self.repository:
            return github_repository

        raise AttributeError


class GitHubPayloadAlertContainer(BaseModel):
    payload: GitHubPayloadAlert | None

    def get_payload(
        self: GitHubPayloadAlertContainer,
    ) -> GitHubPayloadAlert:
        if github_payload := self.payload:
            return github_payload

        raise AttributeError
