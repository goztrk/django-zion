# Django Imports
from django.db import models

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
