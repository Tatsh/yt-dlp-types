from collections.abc import Sequence
from enum import Enum
from http.cookiejar import Cookie

from ._misc import LoggerProtocol

__all__ = ('extract_cookies_from_browser',)


class _LinuxKeyring(Enum):
    BASIC_TEXT = ...
    GNOME_KEYRING = ...
    KWALLET4 = ...
    KWALLET5 = ...
    KWALLET6 = ...


def extract_cookies_from_browser(browser: str,
                                 profile: str = ...,
                                 logger: LoggerProtocol = ...,
                                 *,
                                 keyring: _LinuxKeyring = ...) -> Sequence[Cookie]:
    ...
