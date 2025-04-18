import abc
from email.message import Message
import enum
import io
from types import TracebackType
from typing import Any, IO, TypeAlias, TypeVar
from collections.abc import Callable
from collections.abc import Iterable, Mapping
from typing_extensions import Self

from ..cookies import YoutubeDLCookieJar
from ..utils import classproperty
from ..utils._utils import SupportedLogger
from ..utils.networking import HTTPHeaderDict
from ._helper import wrap_request_errors

DEFAULT_TIMEOUT = ...


def register_preference(*handlers: type[RequestHandler]) -> Callable[[Any], Any]:
    ...


class RequestDirector:
    def __init__(self, logger: SupportedLogger, verbose: bool = ...) -> None:
        ...

    def close(self) -> None:
        ...

    def add_handler(self, handler: RequestHandler) -> None:
        ...

    def send(self, request: Request) -> Response:
        ...


_REQUEST_HANDLERS = ...

_H = TypeVar('_H', bound=type[RequestHandler])


def register_rh(handler: _H) -> _H:
    ...


class Features(enum.Enum):
    ALL_PROXY = ...
    NO_PROXY = ...


class RequestHandler(abc.ABC):
    _SUPPORTED_URL_SCHEMES = ...
    _SUPPORTED_PROXY_SCHEMES = ...
    _SUPPORTED_FEATURES = ...

    def __init__(
        self,
        *,
        logger: SupportedLogger,
        headers: HTTPHeaderDict = ...,
        cookiejar: YoutubeDLCookieJar = ...,
        timeout: float | None = ...,
        proxies: dict[str, str] | None = ...,
        source_address: str | None = ...,
        verbose: bool = ...,
        prefer_system_certs: bool = ...,
        client_cert: dict[str, str | None] | None = ...,
        verify: bool = ...,
        legacy_ssl_support: bool = ...,
        **_: dict[str, Any],
    ) -> None:
        ...

    @wrap_request_errors
    def validate(self, request: Request) -> None:
        ...

    @wrap_request_errors
    def send(self, request: Request) -> Response:
        ...

    def close(self) -> None:
        ...

    @classproperty
    def RH_NAME(self) -> str:
        ...

    @classproperty
    def RH_KEY(self) -> str:
        ...

    def __enter__(self) -> Self:
        ...

    def __exit__(
        self,
        type_: type[BaseException] | None,
        value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        ...


class Request:
    def __init__(
        self,
        url: str,
        data: RequestData = ...,
        headers: Mapping[str, str] | None = ...,
        proxies: dict[str, str] | None = ...,
        query: dict[str, str] | None = ...,
        method: str | None = ...,
        extensions: dict[Any, Any] | None = ...,
    ) -> None:
        ...

    @property
    def url(self) -> str:
        ...

    @url.setter
    def url(self, url: str) -> None:
        ...

    @property
    def method(self) -> str:
        ...

    @method.setter
    def method(self, method: str) -> None:
        ...

    @property
    def data(self) -> RequestData:
        ...

    @data.setter
    def data(self, data: RequestData) -> None:
        ...

    @property
    def headers(self) -> HTTPHeaderDict:
        ...

    @headers.setter
    def headers(self, new_headers: HTTPHeaderDict) -> None:
        ...

    def update(
        self,
        url: str | None = ...,
        data: RequestData | None = ...,
        headers: Mapping[str, str] | None = ...,
        query: Mapping[Any, Any] | None = ...,
        extensions: Mapping[Any, Any] | None = ...,
    ) -> None:
        ...

    def copy(self) -> Self:
        ...


HEADRequest = ...
PUTRequest = ...


class Response(io.IOBase):
    def __init__(
        self,
        fp: io.IOBase,
        url: str,
        headers: Mapping[str, str],
        status: int = ...,
        reason: str | None = ...,
        extensions: dict[Any, Any] | None = ...,
    ) -> None:
        ...

    def readable(self) -> bool:
        ...

    def read(self, amt: int | None = ...) -> bytes:
        ...

    def close(self) -> None:
        ...

    def get_header(self, name: str, default: str | None = ...) -> str:
        ...

    @property
    def code(self) -> int:
        ...

    def getcode(self) -> int:
        ...

    def geturl(self) -> str:
        ...

    def info(self) -> Message[str, str]:
        ...

    def getheader(self, name: str, default: str | None = ...) -> str:
        ...


RequestData: TypeAlias = bytes | Iterable[bytes] | IO[Any] | None
Preference: TypeAlias = Callable[[RequestHandler, Request], int]
_RH_PREFERENCES: set[Preference] = ...
