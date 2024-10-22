from __future__ import annotations

import datetime

from pydantic import (
    BaseModel as BaseModelPydantic,
    ConfigDict,
    FieldSerializationInfo,
    field_serializer,
)

from .helper_utils import create_timestamp_github


class BaseModel(BaseModelPydantic):
    model_config = ConfigDict(
        validate_assignment=True,
        populate_by_name=True,
    )

    @field_serializer(  # trunk-ignore(mypy/misc)
        "answer_chosen_at",
        "closed_at",
        "created_at",
        "pushed_at",
        "timestamp_conversation",
        "timestamp_tagged",
        "updated_at",
        check_fields=False,
    )
    def serialize_timestamp(
        self: BaseModelPydantic,
        timestamp: datetime.datetime | None,
        _info: FieldSerializationInfo,
    ) -> str | None:
        del _info
        if timestamp is None:
            return None

        return create_timestamp_github(
            timestamp=timestamp,
        )
