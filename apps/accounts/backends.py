# Django Imports
from django.contrib.auth.backends import ModelBackend


__all__ = ["EmailBackend"]


class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get("username")
        try:
            user = self.user_model.objects.get(email=username)
        except self.user_model.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None
