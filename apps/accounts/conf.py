# Third Party (PyPI) Imports
from appconf import AppConf

# Django Imports
from django.conf import settings  # noqa


class ZionAccountsAppConf(AppConf):
    class Meta:
        prefix = "zion_accounts"
