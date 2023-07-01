# ZION Shared Library Imports
from zion.apps.account.conf import settings
from zion.apps.account.models import Account


def account(request):
    ctx = {
        "account": Account.for_request(request),
        "ACCOUNT_OPEN_SIGNUP": settings.ACCOUNT_OPEN_SIGNUP,
    }
    return ctx
