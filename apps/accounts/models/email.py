# Third Party (PyPI) Imports
from result import (
    Err,
    Ok,
    Result,
)

# Django Imports
from django.db import models
from django.utils.translation import gettext_lazy as _

# ZION Shared Library Imports
from zion.apps.accounts.conf import settings
from zion.models.mixins import (
    CreateModifyMixin,
    TokenMixin,
)


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
        max_length=254,
        unique=settings.ZION_ACCOUNTS_EMAIL_UNIQUE,
        verbose_name=_("Email Address"),
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
        if settings.ZION_ACCOUNTS_EMAIL_UNIQUE:
            unique_together = ["user", "email"]

    def __str__(self):
        return self.email

    def set_as_primary(self, stop_if_has_primary=False) -> Result[bool, None]:
        """Set this email address as the primary email address."""
        old_primary = EmailAddress.objects.get_primary(user=self.user)
        if old_primary:
            if stop_if_has_primary:
                return Ok(False)
            old_primary.is_primary = False
            old_primary.save()

        self.is_primary = True
        self.save()
        self.user.email = self.email
        self.user.save()

        return Ok()

    def send_confirmation(self, request, **kwargs) -> Result["EmailConfirmation", str]:
        """Send a confirmation email to this email address."""
        if self.is_verified:
            return Err(_("Email address already verified."))

        email_confirmation = self.email_confirmations.last()
        if not email_confirmation:
            email_confirmation = self.email_confirmations.create()

        # TODO: Add email sending logic

        return Ok(email_confirmation)

    def verify(self, token) -> Result[bool, str]:
        """Verify the email address with the given token."""
        if self.is_verified:
            return Err(_("Email address already verified."))

        email_confirmation = self.email_confirmations.filter(token=token).first()

        if not email_confirmation or email_confirmation.token != token:
            return Err(_("Invalid token."))

        self.is_verified = True
        self.set_as_primary(stop_if_has_primary=True)

        return Ok()


class EmailConfirmation(CreateModifyMixin, TokenMixin, models.Model):
    """Email confirmation model.
    In progress
    """

    email_address = models.ForeignKey(
        EmailAddress,
        on_delete=models.CASCADE,
        related_name="email_confirmations",
        verbose_name=_("Email Address"),
    )
    is_sent = models.BooleanField(default=False, verbose_name=_("Sent"))

    class Meta:
        verbose_name = _("Email Confirmation")
        verbose_name_plural = _("Email Confirmations")
        ordering = ["-created"]

    def __str__(self):
        return f"Confirmation for {self.email_address}"
