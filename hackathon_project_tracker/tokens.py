from __future__ import annotations

import os

TOKENS: dict[str, str] = {
    "GITHUB_OWNER": "reflex-dev",
    "GITHUB_REPO": "reflex",
    "GITHUB_CLIENT_ID": os.getenv("GITHUB_CLIENT_ID"),
    "GITHUB_CLIENT_SECRET": os.getenv("GITHUB_CLIENT_SECRET"),
    "OTEL_PROVIDER_TOKEN_NAME": os.getenv("OTEL_PROVIDER_TOKEN_NAME"),
    "OTEL_APP_NAME": os.getenv("OTEL_APP_NAME"),
}
if TOKENS["OTEL_PROVIDER_TOKEN_NAME"] is not None:
    TOKENS.update(
        {
            TOKENS["OTEL_PROVIDER_TOKEN_NAME"]: os.getenv(
                TOKENS["OTEL_PROVIDER_TOKEN_NAME"],
            ),
        },
    )
