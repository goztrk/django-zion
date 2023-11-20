# Third Party (PyPI) Imports
from appconf import AppConf

# Django Imports
from django.conf import settings


__all__ = ["settings"]


class ZionAccountsAppConf(AppConf):
    HOOKS = "zion.apps.accounts.hooks.AccountsHooks"

    class Meta:
        prefix = "zion_accounts"
