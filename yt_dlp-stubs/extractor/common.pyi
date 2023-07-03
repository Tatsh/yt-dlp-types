from typing import Any, Literal, Mapping
import urllib.request

from ..YoutubeDL import YoutubeDL
from ..utils import ExtractorError

__all__ = ('ExtractorError', 'InfoExtractor')


class InfoExtractor:
    def __init__(self, downloader: YoutubeDL | None = ...) -> None:
        ...

    def _download_json(self,
                       url: str | urllib.request.Request,
                       video_id: str,
                       note: str | None = ...,
                       errnote: str | None = ...,
                       transform_source: Any = ...,
                       fatal: bool = ...,
                       encoding: str | None = ...,
                       data: Any = ...,
                       headers: Mapping[str, str] = ...,
                       query: Mapping[str, str] = ...,
                       expected_status: int | None = ...) -> Any:
        ...

    def _real_extract(self, url: str) -> Any:
        ...

    @staticmethod
    def _availability(
        is_private: bool | None = ...,
        needs_premium: bool | None = ...,
        needs_subscription: bool | None = ...,
        needs_auth: bool | None = ...,
        is_unlisted: bool | None = ...
    ) -> Literal['private', 'premium_only', 'subscriber_only', 'needs_auth', 'unlisted',
                 'public'] | None:
        ...

    def _request_webpage(self,
                         url_or_req: str | urllib.request.Request,
                         video_id: str,
                         note: str | None = ...,
                         errnote: str | None = ...,
                         fatal: bool = ...,
                         data: Any = ...,
                         headers: Mapping[str, str] = ...,
                         query: Mapping[str, str] = ...,
                         expected_status: int | None = ...) -> Any:
        ...

    @classmethod
    def _match_id(cls, url: str) -> str:
        ...
