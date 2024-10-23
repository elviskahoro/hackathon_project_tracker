from __future__ import annotations

from datetime import datetime

import reflex as rx
from github import Github

from hackathon_project_tracker import helper_github
from hackathon_project_tracker.otel import tracer
from hackathon_project_tracker.tokens import TOKENS

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

    def on_load(
        self: State,
    ) -> None:
        with tracer.start_as_current_span("on_load"):
            print("on_load")

    def placeholder_function(
        self: State,
    ) -> None:
        with tracer.start_as_current_span("placeholder_function"):
            print("placeholder_function")
