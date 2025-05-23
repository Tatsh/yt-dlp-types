import collections

from typing import Any


def random_user_agent() -> str:
    ...


class HTTPHeaderDict(collections.UserDict[str, Any], dict[str, Any]):  # type: ignore[misc]
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        ...

    def __setitem__(self, key: str, value: Any) -> None:
        ...

    def __getitem__(self, key: Any) -> Any:
        ...

    def __delitem__(self, key: Any) -> None:
        ...

    def __contains__(self, key: Any) -> bool:
        ...


std_headers: HTTPHeaderDict = ...


def clean_proxies(proxies: dict[str, str], headers: HTTPHeaderDict) -> None:
    ...


def clean_headers(headers: HTTPHeaderDict) -> None:
    ...


def remove_dot_segments(path: str) -> str:
    ...


def escape_rfc3986(s: str) -> str:
    ...


def normalize_url(url: str) -> str:
    ...
