# Django Imports
from django import template
from django.utils.safestring import mark_safe

# ZION Shared Library Imports
from zion.apps.js_urls.conf import settings
from zion.apps.js_urls.serializer import get_urls_as_json


register = template.Library()


@register.simple_tag
@mark_safe
def print_js_urls():
    if not settings.ZION_JS_URLS_ENABLED:
        return ""

    js_obj = settings.ZION_JS_URLS_JS_OBJECT_NAME
    urls = get_urls_as_json()
    html = f"<script>{js_obj} = Object.assign({js_obj} || {'{}'}, {urls});</script>"
    return html
