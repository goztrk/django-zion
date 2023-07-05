# Python Standard Library
from enum import IntFlag

# ZION Shared Library Imports
from zion.conf import settings


class Choice(IntFlag):
    def as_dict(self):
        """
        Return choice item as a dict.
        """
        return {
            "name": self.name_str,
            "value": self.value,
            "is_hidden": self.is_hidden,
        }

    @property
    def name_str(self) -> str:
        """
        Converts upper case NAME to Name format. Underscores become spaces.
        """
        if self.name in settings.ZION_CHOICE_NAME_OVERRIDES:
            return settings.ZION_CHOICE_NAME_OVERRIDES[self.name]
        else:
            return " ".join([word.capitalize() for word in self.name.split("_")])

    @property
    def is_hidden(self) -> bool:
        """
        Is the choice item hidden?
        """
        return self in self.hidden_choices()

    @classmethod
    def hidden_choices(cls) -> set:
        """List of hidden choices from user or model
        Override this on derived Choice.
        """
        return {}

    @classmethod
    def choices(cls) -> dict:
        """
        Returns choices dict for easy usage especially in JS
        """
        return {enum_obj.name: enum_obj.as_dict() for enum_obj in cls}

    @classmethod
    def model_choices(cls, include_hidden=False):
        """
        Return (value, name,) tuple of list from the choices for usage in Model
        """
        return [
            (
                enum_obj.value,
                enum_obj.name_str,
            )
            for enum_obj in cls
            if include_hidden or not enum_obj.is_hidden
        ]
