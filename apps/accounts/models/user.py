# Python Standard Library
from typing import Any

# Django Imports
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as DjangoUserManager


class UserManager(DjangoUserManager):
    def _create_user(self, username, email, password, **extra_fields):
        should_create_email = extra_fields.pop("should_create_email", True)
        user = super()._create_user(username, email, password, **extra_fields)

        if user and should_create_email:
            user.email_addresses.create(email=email)

        return user

    def create_superuser(
        self,
        username: str,
        email: str | None,
        password: str | None,
        **extra_fields: Any
    ) -> Any:
        user = super().create_superuser(
            username, email, password, should_create_email=False, **extra_fields
        )
        user.email_addresses.create(email=email, is_primary=True, is_verified=True)

        return user


class User(AbstractUser):
    objects = UserManager()
