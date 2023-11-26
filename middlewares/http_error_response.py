# ZION Shared Library Imports
from zion.utils.exceptions import HttpResponseError


class HttpErrorResponseMiddleware:
    """This middleware allows `HttpResponseError`s to be thrown to short-circuit
    processing of a view, and allows a response to be returned instead.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def process_exception(self, request, exception):
        if isinstance(exception, HttpResponseError):
            return exception.response

        return None
