from typing import Any

from ..utils import YoutubeDLError
from .common import RequestHandler, Response

class RequestError(YoutubeDLError):
    def __init__(
        self,
        msg: str | None = ...,
        cause: Exception | str | None = ...,
        handler: RequestHandler = ...,
    ) -> None: ...

class UnsupportedRequest(RequestError): ...

class NoSupportingHandlers(RequestError):
    def __init__(
        self, unsupported_errors: list[UnsupportedRequest], unexpected_errors: list[Exception]
    ) -> None: ...

class TransportError(RequestError): ...

class HTTPError(RequestError):
    response: Response
    status: int
    reason: str | None
    redirect_loop: bool
    def __init__(self, response: Response, redirect_loop: bool = ...) -> None: ...
    def close(self) -> None: ...

class IncompleteRead(TransportError):
    def __init__(self, partial: int, expected: int | None = ..., **kwargs: Any) -> None: ...

class SSLError(TransportError): ...
class CertificateVerifyError(SSLError): ...
class ProxyError(TransportError): ...

network_exceptions = ...
