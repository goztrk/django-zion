# Third Party (PyPI) Imports
from appconf import AppConf

# Django Imports
from django.conf import settings  # noqa


class ViteAppConfig(AppConf):
    MANIFEST_PATH = settings.BASE_DIR / "static/js"
    URL_PATH = f"{settings.STATIC_URL}js"
    MANIFEST_FILE = "manifest.json"
    MANIFEST_DEV_FILE = "manifest.dev.json"

    DEV_SERVER_PROTOCOL = "http"
    DEV_SERVER_HOST = "localhost"
    DEV_SERVER_PORT = 3000
    WS_CLIENT_URL = "@vite/client"

    class Meta:
        prefix = "zion_vite"
