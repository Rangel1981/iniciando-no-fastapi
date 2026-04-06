from pydantic import BaseModel

class BaseSchemas(BaseModel):
    class config:
        extra = 'forbid'
        from_attributes = True