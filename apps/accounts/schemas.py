# Python Standard Library
import datetime
from typing import Annotated

# Third Party (PyPI) Imports
from pydantic import (
    EmailStr,
    StringConstraints,
)

# ZION Shared Library Imports
from zion.utils import ModelSchema


class UserSchema(ModelSchema):
    id: int
    username: Annotated[str, StringConstraints(max_length=150)]
    first_name: Annotated[str, StringConstraints(max_length=150)] | None = None
    last_name: Annotated[str, StringConstraints(max_length=150)] | None = None
    email: EmailStr
    created: datetime.datetime
    modified: datetime.datetime
