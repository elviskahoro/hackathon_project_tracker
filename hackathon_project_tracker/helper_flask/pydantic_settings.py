from pydantic import (
    BaseModel as BaseModelPydantic,
    ConfigDict,
)


class BaseModel(BaseModelPydantic):
    model_config = ConfigDict(
        validate_assignment=True,
        populate_by_name=True,
    )
