# Third Party (PyPI) Imports
from nanoid import generate

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


class TokenMixin(models.Model):
    """
    A mixin that provides a ``token`` field.

    Usage:
        class MyModel(TokenMixin, token_size=32, editable=False):
            pass
    """

    TOKEN_SIZE: int
    TOKEN_EDITABLE: bool

    class Meta:
        abstract = True

    def __init_subclass__(cls, **kwargs) -> None:
        cls.TOKEN_SIZE = kwargs.pop("token_size", 32)
        cls.TOKEN_EDITABLE = kwargs.pop("token_editable", False)

        super().__init_subclass__(**kwargs)

        cls.token = models.CharField(
            _("Token"),
            max_length=cls.TOKEN_SIZE,
            unique=True,
            default=cls._generate_token,
            editable=cls.TOKEN_EDITABLE,
        )

    @classmethod
    def _generate_token(cls) -> str:
        return generate(size=cls.TOKEN_SIZE)

    def generate_token(self) -> None:
        self.token = self._generate_token()
        self.save()
