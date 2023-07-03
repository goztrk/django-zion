# Third Party (PyPI) Imports
from appconf import AppConf

# Django Imports
from django.conf import settings  # noqa


class JsUrls(AppConf):
    ENABLED = True
    ALLOWED = []
    JS_OBJECT_NAME = "window.Site"

    class Meta:
        prefix = "zion_js_urls"
