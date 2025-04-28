from enum import Enum
from http.cookiejar import Cookie, MozillaCookieJar
from http.cookies import SimpleCookie
from typing import Any, TextIO
from collections.abc import Iterator

from .minicurses import MultilinePrinter

from .YoutubeDL import YoutubeDL

from ._misc import LoggerProtocol

CHROMIUM_BASED_BROWSERS: set[str] = ...
SUPPORTED_BROWSERS: set[str] = ...


class _LinuxKeyring(Enum):
    BASIC_TEXT = ...
    GNOME_KEYRING = ...
    KWALLET4 = ...
    KWALLET5 = ...
    KWALLET6 = ...


class YDLLogger(LoggerProtocol):
    class ProgressBar(MultilinePrinter):
        ...

    def progress_bar(self) -> ProgressBar:
        ...


class YoutubeDLCookieJar(MozillaCookieJar):
    def __init__(self, filename: str | None = ..., *args: Any, **kwargs: Any) -> None:
        ...

    def open(self, file: str, *, write: bool = ...) -> Iterator[TextIO]:
        ...

    def get_cookie_header(self, url: str) -> str:
        ...

    def get_cookies_for_url(self, url: str) -> list[Cookie]:
        ...


def load_cookies(cookie_file: str, browser_specification: str | None,
                 ydl: YoutubeDL) -> YoutubeDLCookieJar:
    ...


def extract_cookies_from_browser(browser: str,
                                 profile: str | None = ...,
                                 logger: LoggerProtocol = ...,
                                 *,
                                 keyring: _LinuxKeyring | None = ...,
                                 container: str | None = ...) -> YoutubeDLCookieJar:
    ...


class ChromeCookieDecryptor:
    def decrypt(self, encrypted_value: bytes) -> str:
        ...


class LinuxChromeCookieDecryptor(ChromeCookieDecryptor):
    def __init__(self,
                 browser_keyring_name: str,
                 logger: LoggerProtocol,
                 *,
                 keyring: _LinuxKeyring | None = ...,
                 meta_version: int | None = ...) -> None:
        ...

    @staticmethod
    def derive_key(password: bytes) -> bytes:
        ...


class MacChromeCookieDecryptor(ChromeCookieDecryptor):
    @staticmethod
    def derive_key(password: bytes) -> bytes:
        ...


class WindowsChromeCookieDecryptor(ChromeCookieDecryptor):
    @staticmethod
    def derive_key(password: bytes) -> bytes:
        ...


def get_cookie_decryptor(browser_root: Any,
                         browser_keyring_name: str,
                         logger: LoggerProtocol,
                         *,
                         keyring: _LinuxKeyring | None = ...,
                         meta_version: int | None = ...) -> ChromeCookieDecryptor:
    ...


class ParserError(Exception):
    ...


class DataParser:
    ...


def pbkdf2_sha1(password: bytes, salt: bytes, iterations: int, key_length: int) -> bytes:
    ...


class LenientSimpleCookie(SimpleCookie):
    ...
