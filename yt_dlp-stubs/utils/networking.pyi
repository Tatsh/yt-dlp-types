from collections.abc import Mapping
from typing import Any, TypeVar, overload
from typing_extensions import Self

from ._utils import NO_DEFAULT
from collections import UserDict


def random_user_agent() -> str:
    ...


_T = TypeVar('_T')


class HTTPHeaderDict(UserDict[str, str]):
    def __new__(cls, *args: Any, **kwargs: Any) -> Self:
        ...

    def __init__(self, /, *args: object, **kwargs: object) -> None:
        ...

    def sensitive(self, /) -> dict[str, str]:
        ...

    @overload
    def get(self, key: str, /) -> str | None:
        ...

    @overload
    def get(self, key: str, /, default: _T) -> str | _T:
        ...

    @overload
    def get(self, key: str, /, default: type[NO_DEFAULT] | _T = ...) -> str | _T | type[NO_DEFAULT]:
        ...

    @overload
    def pop(self, key: str, /) -> str:
        ...

    @overload
    def pop(self, key: str, /, default: _T) -> str | _T:
        ...

    @overload
    def pop(self,
            key: str,
            /,
            default: type[NO_DEFAULT] | _T | str = ...) -> str | _T | type[NO_DEFAULT]:
        ...

    @overload
    def setdefault(self, key: str, /) -> str:
        ...

    @overload
    def setdefault(self, key: str, /, default: str) -> str:
        ...

    @overload
    def setdefault(self, key: str, /, default: str | None = None) -> str:
        ...

    def update(self, other: Mapping[str, str], /, **kwargs: str) -> None:  # type: ignore[override]
        ...


std_headers: HTTPHeaderDict


def clean_proxies(proxies: dict[str, object], headers: HTTPHeaderDict) -> None:
    ...


def clean_headers(headers: HTTPHeaderDict) -> None:
    ...


def remove_dot_segments(path: str) -> str:
    ...


def escape_rfc3986(s: str) -> str:
    ...


def normalize_url(url: str) -> str:
    ...


def select_proxy(url: str, proxies: Mapping[str, object]) -> str:
    ...
