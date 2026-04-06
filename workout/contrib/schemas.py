from typing import Annotated

from pydantic import Field, BaseModel

from workout.contrib.schemas import BaseSchemas


class BaseSchemas(BaseModel):
    model_config = {"extra": "forbid", "from_attributes": True}
