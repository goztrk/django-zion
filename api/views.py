# Python Standard Library
from typing import Type

# Django Imports
from django.forms import Form
from django.http import HttpResponse
from django.views import View

# ZION Shared Library Imports
from zion.utils import Schema


class ErrorSchema(Schema):
    message: str


class FormErrorSchema(Schema):
    field_errors: dict[str, list[str]]
    non_field_errors: list[str]


class APIView(View):
    def ok(self, data: Type[Schema]):
        """Returns a 200 response with the data passed in"""
        return self.response(data, status=200)

    def err(self, data: Type[Schema] | Type[Form] | str, status: int = 400):
        """Returns a 400 response with the data passed in"""
        if status < 400 or status > 499:
            raise ValueError("Status code must be between 400 and 499")

        if isinstance(data, str):
            data = ErrorSchema(message=data)
        elif issubclass(data, Form):
            data = FormErrorSchema(
                field_errors=data.errors,
                non_field_errors=data.non_field_errors(),
            )

        return self.response(data, status=status)

    def not_found(self, data: Type[Schema] | str = "Not Found"):
        """Returns a 404 response with the data passed in"""
        return self.err(data, status=404)

    def forbidden(self, data: Type[Schema] | str = "Forbidden"):
        """Returns a 403 response with the data passed in"""
        return self.err(data, status=403)

    def response(self, data: Type[Schema], status: int = 200):
        if not isinstance(status, int):
            raise TypeError("Status must be an integer")
        elif status < 200 or status > 499:
            raise ValueError("Status must be between 200 and 499")

        return HttpResponse(
            data.model_dump_json(), status=status, content_type="application/json"
        )


# Sample Usage:


class PaginatorSchema(Schema):
    p: int | None = None


class SampleAPIView(APIView):
    def get(self, request, *args, **kwargs):
        return self.ok({})
