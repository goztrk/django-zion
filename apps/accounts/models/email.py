# Third Party (PyPI) Imports
from result import (
    Ok,
    Result,
)

# Django Imports
from django.db import models
from django.utils.translation import gettext_lazy as _

# ZION Shared Library Imports
from zion.apps.accounts.conf import settings
from zion.models.mixins import CreateModifyMixin


class EmailManager(models.Manager):
    def get_primary(self, user):
        """Return the user's primary email address."""
        return self.get(user=user, is_primary=True)


class EmailAddress(CreateModifyMixin, models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("User"),
        related_name="email_addresses",
        on_delete=models.CASCADE,
    )
    email = models.EmailField(
        max_length=254, unique=True, verbose_name=_("Email Address")
    )
    is_primary = models.BooleanField(
        default=False, verbose_name=_("Primary Email Address")
    )
    is_verified = models.BooleanField(default=False, verbose_name=_("Verified"))

    objects = EmailManager()

    class Meta:
        verbose_name = _("Email")
        verbose_name_plural = _("Emails")
        ordering = ["-is_primary", "-is_verified", "-created"]

    def __str__(self):
        return self.email

    def set_as_primary(self, conditional=False) -> Result[bool, None]:
        """Set this email address as the primary email address."""
        old_primary = EmailAddress.objects.get_primary(user=self.user)
        if old_primary:
            if conditional:
                return Ok(False)
            old_primary.is_primary = False
            old_primary.save()

        self.is_primary = True
        self.save()
        self.user.email = self.email
        self.user.save()

        return Ok(True)


class EmailConfirmation(CreateModifyMixin, models.Model):
    """Email confirmation model.
    In progress
    """

    email_address = models.ForeignKey(
        EmailAddress, on_delete=models.CASCADE, verbose_name=_("Email Address")
    )
    token = models.CharField(max_length=64, unique=True, verbose_name=_("Token"))

    class Meta:
        verbose_name = _("Email Confirmation")
        verbose_name_plural = _("Email Confirmations")
        ordering = ["-created"]

    def __str__(self):
        return f"Confirmation for {self.email_address}"
