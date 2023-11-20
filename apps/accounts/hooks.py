# ZION Shared Library Imports
from zion.apps.accounts.conf import settings


__all__ = ["AccountsHooks", "hooks"]


class AccountsHooks:
    ...


class HookProxy:
    def __getattr__(self, attr):
        return getattr(settings.ZION_ACCOUNTS_HOOKS, attr)


hooks = HookProxy()
