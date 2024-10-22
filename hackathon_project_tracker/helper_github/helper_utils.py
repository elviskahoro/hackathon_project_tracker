from __future__ import annotations

from typing import TYPE_CHECKING, Any

DEFAULT_GITHUB_PREFIX: str = "GH"
DEFAULT_TIME_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
DEFAULT_TIME_ZONE: str = "US/Pacific"

if TYPE_CHECKING:
    import datetime


def add_github_prefix(
    string_to_prefix: str,
    github_prefix: str | None = None,
) -> str:
    if github_prefix is None:
        github_prefix = DEFAULT_GITHUB_PREFIX

    return f"{github_prefix}-{string_to_prefix}"


def create_timestamp_github(
    timestamp: datetime.datetime | None,
) -> str:
    if timestamp is None:
        raise AttributeError

    return timestamp.strftime(DEFAULT_TIME_FORMAT)


def traverse_markdown_document(
    node: Any,  # noqa: ANN401
) -> list[str]:
    """Marko parses text into a tree representation.

    Starts at the top of the tree and traverses the to the leaves returning a list of all the strings.
    This allows for more precision when applying regex, since we're applying per content object i.e. heading, paragraph, etc.
    """
    children = None
    try:
        children = node.children

    except AttributeError:
        return []

    if children is None:
        return []

    if isinstance(
        children,
        str,
    ):
        return [children]

    output: list[str] = []
    for child in children:
        if content := traverse_markdown_document(
            node=child,
        ):
            output.extend(content)

    return output
