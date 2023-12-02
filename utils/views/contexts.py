# Python Standard Library
from socket import gethostname

# ZION Shared Library Imports
from zion.conf import settings


__all__ = ["wrap_context"]


def wrap_context(request, data={}):
    context = {}
    context["site_name"] = settings.ZION_SITE_NAME
    context["DEBUG"] = settings.DEBUG
    context["server"] = {"hostname": gethostname()}

    # Allow overriding the values in case it is needed
    context.update(data)

    return context
