# Third Party (PyPI) Imports
from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
)


__all__ = ["Schema", "Field"]


class Schema(BaseModel):
    ...


class ModelSchema(Schema):
    model_config = ConfigDict(from_attributes=True)
