# Python Standard Library
import os
import typing as t
from urllib.parse import urljoin

# Django Imports
from django import template
from django.utils.safestring import mark_safe

# ZION Shared Library Imports
from zion.apps.vite.conf import settings
from zion.apps.vite.resolver import resolve_assets


register = template.Library()


def _generate_script_tag(src: str, attrs: t.Dict[str, str]) -> str:
    attrs_str = " ".join([f'{key}="{value}"' for key, value in attrs.items()])
    return f'<script {attrs_str} src="{src}"></script>'


@register.simple_tag
@mark_safe
def vite_asset(path):
    assets = resolve_assets()
    return _generate_script_tag(assets[path], {"type": "module"})


@register.simple_tag
@mark_safe
def vite_hmr_client():
    manifest_dev_file = os.path.join(
        settings.ZION_VITE_MANIFEST_PATH, settings.ZION_VITE_MANIFEST_DEV_FILE
    )
    if settings.DEBUG and os.path.exists(manifest_dev_file):
        url = urljoin(
            f"{settings.ZION_VITE_DEV_SERVER_PROTOCOL}://"
            f"{settings.ZION_VITE_DEV_SERVER_HOST}:{settings.ZION_VITE_DEV_SERVER_PORT}",
            urljoin(settings.ZION_VITE_URL_PATH, settings.ZION_VITE_WS_CLIENT_URL),
        )
        return _generate_script_tag(url, {"type": "module"})
    else:
        return ""
