from __future__ import annotations

from enum import Enum

from pydantic.dataclasses import dataclass

from .pydantic_settings import BaseModel  # trunk-ignore(ruff/TCH001)


class ResponseCode(Enum):
    ACCEPTED_AND_SUCCESSFUL = 200
    ACCEPTED_WITH_NOTHING_TO_DO = 202
    FAILURE_WITH_RETRY = 429
    FAILURE_WITH_NO_RETRY = 405


class PydanticConfiguration:
    arbitrary_types_allowed = True


@dataclass(
    config=PydanticConfiguration,
)
class ResponseStatus:
    response_string: str | None
    response_code: ResponseCode
    response_dict: BaseModel | None = None

    def __repr__(
        self: ResponseStatus,
    ) -> str:
        return f"{self.response_code.value} : {self.response_code.name} : {self.response_string}"

    @classmethod
    def from_response_code(
        cls: type[ResponseStatus],
        response_code: ResponseCode,
    ) -> ResponseStatus:
        return ResponseStatus(
            response_string=response_code.name,
            response_code=response_code,
        )

    def get_return_response_dict(
        self: ResponseStatus,
    ) -> BaseModel:
        response_dict: BaseModel | None = self.response_dict
        if response_dict is None:
            raise AttributeError

        return response_dict

    def get_return_response_with_dict(
        self: ResponseStatus,
    ) -> tuple[BaseModel, int]:
        return self.get_return_response_dict(), self.response_code.value

    def get_return_response_string(
        self: ResponseStatus,
    ) -> str:
        response_string: str | None = self.response_string
        if response_string is None:
            raise AttributeError

        return response_string

    def get_return_response_tuple_with_string(
        self: ResponseStatus,
    ) -> tuple[str, int]:
        return self.get_return_response_string(), self.response_code.value
