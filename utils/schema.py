# Third Party (PyPI) Imports
from pydantic import (
    BaseModel,
    Field,
)


__all__ = ["Schema", "Field"]


class Schema(BaseModel):
    class Config:
        from_attributes = True  # aka orm_mode
