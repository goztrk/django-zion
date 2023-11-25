# Third Party (PyPI) Imports
from nanoid import generate
from nanoid.resources import alphabet as DEFAULT_ALPHABET

# Django Imports
from django.db import models
from django.utils.translation import gettext_lazy as _

# ZION Shared Library Imports
from zion.conf import settings


class TimeZoneField(models.CharField):
    def __init__(self, *args, **kwargs):
        defaults = {
            "max_length": 100,
            "default": "",
            "choices": settings.ZION_TIMEZONES,
            "blank": True,
        }
        defaults.update(kwargs)
        return super(TimeZoneField, self).__init__(*args, **defaults)


class TokenField(models.CharField):
    def __init__(self, *args, **kwargs):
        self.alphabet = kwargs.pop("alphabet", DEFAULT_ALPHABET)
        defaults = {
            "max_length": 32,
            "unique": True,
            "editable": False,
            "verbose_name": _("Token"),
        }
        defaults["default"] = self._generate_token
        defaults.update(kwargs)
        return super(TokenField, self).__init__(*args, **defaults)

    def _generate_token(self) -> str:
        return generate(alphabet=self.alphabet, size=self.max_length)
