# Third Party (PyPI) Imports
from appconf import AppConf

# Django Imports
from django.conf import settings


__all__ = ["settings"]


class ZionAccountsAppConf(AppConf):
    # Allow users to sign up different accounts with same email address
    EMAIL_UNIQUE = True
    # Require email confirmation before login
    EMAIL_CONFIRMATION_REQUIRED = False
    # functions that are exposed to project. Can be overridden in settings.py
    HOOKS = "zion.apps.accounts.hooks.AccountsHooks"

    class Meta:
        prefix = "zion_accounts"
