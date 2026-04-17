from datetime import datetime
from typing import Annotated
from pydantic import UUID4, Field, BaseModel

# A linha 5 foi removida daqui


class BaseSchemas(BaseModel):
    model_config = {"extra": "forbid", "from_attributes": True}


class OutMixin(BaseModel):
    id: Annotated[UUID4, Field(description="Identificador")]
    created_at: Annotated[datetime, Field(description="Data de criação do registro")]
