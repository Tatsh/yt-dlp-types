from enum import Enum
from http.cookiejar import Cookie
from typing import Sequence

from ._misc import LoggerProtocol

__all__ = ('extract_cookies_from_browser',)


class _LinuxKeyring(Enum):
    KWALLET4 = ...
    KWALLET5 = ...
    KWALLET6 = ...
    GNOME_KEYRING = ...
    BASIC_TEXT = ...


def extract_cookies_from_browser(browser: str,
                                 profile: str = ...,
                                 logger: LoggerProtocol = ...,
                                 *,
                                 keyring: _LinuxKeyring = ...) -> Sequence[Cookie]:
    ...
