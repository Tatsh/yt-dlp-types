from inspect import Traceback
from typing import Any, Callable, Literal, Type, TypeVar
import urllib.request

__all__ = ('ExtractorError', 'HEADRequest', 'YoutubeDLError', 'int_or_none', 'parse_iso8601',
           'try_get')

T = TypeVar('T')
U = TypeVar('U')


def try_get(x: T, getter: Callable[[T], U], t: Type[U]) -> U:
    ...


def parse_iso8601(s: str, delimiter: str) -> int | None:
    ...


def int_or_none(x: Any) -> int | None:
    ...


class HEADRequest(urllib.request.Request):
    def get_method(self) -> Literal['HEAD']:
        ...


class NO_DEFAULT:
    ...


def sanitize_filename(s: str, restricted: bool = ..., is_id: bool | NO_DEFAULT = ...) -> str:
    ...


class YoutubeDLError(Exception):
    """Base exception for YoutubeDL errors."""
    def __init__(self, msg: str | None = ...) -> None:
        ...


class ExtractorError(YoutubeDLError):
    """Error during info extraction."""
    def __init__(self,
                 msg: str,
                 tb: Traceback | None = ...,
                 expected: bool = ...,
                 cause: BaseException | None = ...,
                 video_id: str | None = ...,
                 ie: str | None = ...) -> None:
        ...

    def format_traceback(self) -> str:
        ...

    @property
    def __msg(self) -> str:
        ...
