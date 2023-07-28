# Third Party (PyPI) Imports
from appconf import AppConf

# Django Imports
from django.conf import settings  # noqa

# ZION Shared Library Imports
from zion.constants.languages import LANGUAGES
from zion.constants.timezones import TIMEZONES


class ZionAppConf(AppConf):
    CONTEXT_RENDERER = "zion.utils.views.context_renderer"
    SITE_NAME = "Zion"
    DEFAULT_HTTP_PROTOCOL = "http"

    CHOICE_NAME_OVERRIDES = {}

    TIMEZONES = TIMEZONES
    LANGUAGES = LANGUAGES

    class Meta:
        prefix = "zion"
