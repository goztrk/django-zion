# ZION Shared Library Imports
from zion.utils.views import wrap_context


def wrapper(request):
    """Wrap the context with zion data"""
    return wrap_context(request)
