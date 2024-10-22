from __future__ import annotations

import logging
from enum import Enum
from logging import Logger
from pathlib import Path
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from helper_flask import ResponseCode

DEFAULT_FOLDER_PATH_LOGGING: Path = Path.cwd() / "out" / "logs"

LOGGER: Logger | None = None


class Severity(Enum):
    """The severity levels that are available to the user."""

    CRITICAL = "CRITICAL"
    ERROR = "ERROR"
    WARNING = "WARNING"
    INFO = "INFO"
    DEBUG = "DEBUG"
    ALL = "ALL"

    def get_logging_level(
        self: Severity,
    ) -> int:
        """Returns the logging level from the severity enum."""
        match self:

            case Severity.CRITICAL:
                return logging.CRITICAL

            case Severity.ERROR:
                return logging.ERROR

            case Severity.WARNING:
                return logging.WARNING

            case Severity.INFO:
                return logging.INFO

            case Severity.DEBUG:
                return logging.DEBUG

            case Severity.ALL:
                return 0

            case _:
                raise ValueError


def create_log_message(
    the_log: str,
    file: str | None,
) -> str:
    file_name: str | None = Path(file).name if file else None
    return f"{file_name} :: {the_log}" if file_name else the_log


def log(
    the_log: str,
    severity: Severity,
    file: str,
) -> None:
    """Logs a message or dictionary and also prints it out to the console."""
    global LOGGER
    msg: str = create_log_message(
        the_log=the_log,
        file=file,
    )

    if LOGGER is None:
        LOGGER = setup_logger(
            file_name=None,
            logger=None,
            severity_to_show=severity,
        )

    if LOGGER is None:
        error_msg: str = "Logger is null"
        raise OSError(
            error_msg,
        )

    LOGGER.log(
        msg=msg,
        level=severity.get_logging_level(),
    )

    if severity.get_logging_level() >= LOGGER.level:
        print(
            f"{severity.value} : {msg}",
        )


class CustomException(Exception):
    """A custom exception class so that we can match a concrete exception using pattern matching."""

    response_code: ResponseCode | None = None
    severity: Severity

    def set_severity(
        self: CustomException,
        severity: Severity | None,
    ) -> None:
        if severity is None:
            log(
                the_log="Severity cannot be set because it's null",
                severity=Severity.WARNING,
                file=__file__,
            )
            return

        if severity and isinstance(severity, Severity):
            self.severity = severity
            return

        error_msg: str = (
            f"Custom Exception: Trying to set a severity that is not eligible to be attached to a custom exception: {severity.name}."
        )
        raise ValueError(
            error_msg,
        )

    def set_response_code(
        self: CustomException,
        response_code: ResponseCode | None,
    ) -> None:
        self.response_code = response_code

    def get_response_code(
        self: CustomException,
    ) -> ResponseCode:
        if response_code := self.response_code:
            return response_code

        error_msg: str = (
            "Custom Exception: Response Code could not be fetched, it's null"
        )
        raise AttributeError(error_msg)


def log_an_exception(
    exception: Exception,
    file: str,
    severity: Severity = Severity.DEBUG,
) -> None:
    """Takes an exception and logs."""
    log(
        the_log=f"Exception : {type(exception)} : {exception!s}",
        severity=severity,
        file=file,
    )


def log_with_exception(
    the_log: dict | str,
    severity: Severity,
    file: str | None,
    response_code: ResponseCode | None = None,
) -> Any:  # noqa: ANN401
    custom_exception: CustomException = CustomException()
    match the_log:

        case str():
            msg: str = create_log_message(
                the_log=the_log,
                file=file,
            )
            custom_exception = CustomException(
                msg,
            )

        case dict():
            custom_exception = CustomException(
                the_log,
            )

        case _:
            raise ValueError

    custom_exception.set_response_code(
        response_code=response_code,
    )
    custom_exception.set_severity(
        severity=severity,
    )
    return custom_exception


def setup_logger(
    file_name: str | None,
    logger: Logger | None,
    severity_to_show: Severity = Severity.ALL,
) -> Logger:
    """Sets up the logger."""
    if logger is not None and file_name is not None:
        error_msg: str = "Cannot set logger and filename at the same time."
        raise ValueError(
            error_msg,
        )

    global LOGGER
    if LOGGER is not None:
        return LOGGER

    if logger is not None:
        LOGGER = logger
        return LOGGER

    if file_name is not None:
        logging.basicConfig(
            filename=DEFAULT_FOLDER_PATH_LOGGING / file_name,
            encoding="utf-8",
            level=severity_to_show.get_logging_level(),
            force=True,
        )

    else:
        logging.basicConfig(
            encoding="utf-8",
            level=severity_to_show.get_logging_level(),
            force=True,
        )

    LOGGER = logging.getLogger()
    return LOGGER
