# Django Imports
from django.db import models
from django.utils.translation import gettext_lazy as _


class CreateModifyMixin(models.Model):
    """
    A mixin that provides self-updating ``created`` and ``modified`` fields.
    """

    created = models.DateTimeField(_("Created At"), auto_now_add=True)
    modified = models.DateTimeField(_("Modified At"), auto_now=True)

    class Meta:
        abstract = True
