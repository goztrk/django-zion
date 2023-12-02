# Django Imports
from django.urls import path

# ZION Shared Library Imports
from zion.apps.accounts import views


app_name = "accounts"
urlpatterns = [
    path("login", views.Login.as_view(), name="login"),
]
