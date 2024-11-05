import urllib.request
from collections.abc import Callable
from inspect import Traceback
from typing import Any, Literal, TypeVar, override

__all__ = ('ExtractorError', 'HEADRequest', 'YoutubeDLError', 'int_or_none', 'parse_iso8601',
           'sanitize_filename', 'try_get', 'unified_timestamp')

_T = TypeVar('_T')
_U = TypeVar('_U')


def try_get(src: _T, getter: Callable[[_T], _U], type_: type[_U] = ...) -> _U | None:
    ...


def parse_iso8601(s: str, delimiter: str) -> int | None:
    ...


def int_or_none(x: Any) -> int | None:
    ...


class HEADRequest(urllib.request.Request):
    @override
    def get_method(self) -> Literal['HEAD']:
        ...


class NO_DEFAULT:  # noqa: N801
    ...


def sanitize_filename(s: str, restricted: bool = ..., is_id: bool | NO_DEFAULT = ...) -> str:
    ...


class YoutubeDLError(Exception):
    def __init__(self, msg: str | None = ...) -> None:
        ...


class ExtractorError(YoutubeDLError):
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


def unified_timestamp(date_str: str | None, day_first: bool = ...) -> int | float | None:
    ...
