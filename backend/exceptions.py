from __future__ import annotations


class BackendException(BaseException):
    """Base exception for all exceptions in this module"""


class AccessForbidden(BackendException):
    def __init__(self, status_code: int) -> None:
        super().__init__(f"API returned {status_code}")


class ValidationError(BackendException):
    def __init__(self, status_code: int, payload: dict) -> None:
        self.payload = payload
        super().__init__(
            f"API returned {status_code}. This usually occurs to arguments not being specified or the API being unable to process this request. ",
            payload,
        )
