import types
import urllib.request
from _typeshed import Unused
from asyncio.events import AbstractEventLoop
from collections.abc import Awaitable, Callable, Collection, Mapping
from http.client import HTTPResponse
from http.cookiejar import CookieJar
from subprocess import Popen
from typing import Any, AnyStr, Generic, TypeVar
from typing_extensions import Self

has_certifi: bool
has_websockets: bool
_T = TypeVar('_T')


class WebSocketsWrapper(Generic[_T]):
    pool: _T | None
    loop: AbstractEventLoop
    conn: object

    def __init__(self,
                 url: str,
                 headers: Mapping[str, str] | None = None,
                 connect: bool = True,
                 **ws_kwargs: object) -> None:
        ...

    def __enter__(self) -> Self:
        ...

    def send(self, *args: object) -> None:
        ...

    def recv(self, *args: object) -> bytes:
        ...

    def __exit__(self, type: type[BaseException] | None, value: BaseException | None,
                 traceback: types.TracebackType | None) -> None:
        ...

    @staticmethod
    def run_with_loop(main: Awaitable[_T], loop: AbstractEventLoop) -> _T:
        ...


def load_plugins(name: str, suffix: str, namespace: dict[str, object]) -> dict[str, type[object]]:
    ...


def traverse_dict(dictn: Mapping[str, object],
                  keys: Collection[str],
                  casesense: bool = True) -> object:
    ...


def decode_base(value: str, digits: str) -> int:
    ...


def platform_name() -> str:
    ...


def get_subprocess_encoding() -> str:
    ...


def register_socks_protocols() -> None:
    ...


def handle_youtubedl_headers(headers: dict[str, object]) -> dict[str, object]:
    ...


def request_to_url(req: urllib.request.Request | str) -> str:
    ...


def sanitized_Request(url: str, *args: object, **kwargs: object) -> urllib.request.Request:
    ...


class YoutubeDLHandler(urllib.request.AbstractHTTPHandler):
    def __init__(self, params: Mapping[str, object], *args: object, **kwargs: object) -> None:
        ...


YoutubeDLHTTPSHandler = YoutubeDLHandler


class YoutubeDLCookieProcessor(urllib.request.HTTPCookieProcessor):
    def __init__(self, cookiejar: CookieJar | None = None) -> None:
        ...

    def http_response(self, request: urllib.request.Request,
                      response: HTTPResponse) -> HTTPResponse:
        ...

    https_request: Callable[[urllib.request.HTTPCookieProcessor, urllib.request.Request],
                            HTTPResponse]  # type: ignore[assignment]
    https_response = http_response


def make_HTTPS_handler(params: Mapping[str, object], **kwargs: object) -> YoutubeDLHTTPSHandler:
    ...


def process_communicate_or_kill(p: Popen[Any], *args: object,
                                **kwargs: object) -> tuple[AnyStr, AnyStr]:
    ...


def encodeFilename(s: str, for_subprocess: Unused = False) -> bytes:
    ...


def decodeFilename(b: bytes, for_subprocess: Unused = False) -> str:
    ...


def decodeArgument(b: _T) -> _T:
    ...


def decodeOption(optval: AnyStr) -> str:
    ...


def error_to_compat_str(err: object) -> str:
    ...
