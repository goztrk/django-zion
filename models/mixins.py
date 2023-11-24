# Django Imports
from django.db import models


class CreateUpdateMixin(models.Model):
    """
    A mixin that provides self-updating ``created`` and ``modified`` fields.
    """

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
