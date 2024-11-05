import urllib.request
import xml.etree.ElementTree as ET
from collections.abc import Callable, Iterable, Mapping
from typing import Any, Literal, Required, TypedDict

from ..utils import ExtractorError
from ..YoutubeDL import YoutubeDL

__all__ = ('ExtractorError', 'InfoExtractor')


class InfoDict(TypedDict, total=False):
    age_limit: int
    availability: Literal['private', 'premium_only', 'subscriber_only', 'needs_auth', 'unlisted',
                          'public'] | None
    creator: str | None
    comment_count: int | None
    duration: int | None
    formats: list[Any] | None
    id: Required[str]
    like_count: int | None
    tags: list[str] | None
    thumbnail: str | None
    timestamp: int | float | None
    title: str | None
    uploader: str | None
    url: str | None


class InfoExtractor:
    def __init__(self, downloader: YoutubeDL | None = ...) -> None:
        ...

    def _download_json(self,
                       url_or_request: str | urllib.request.Request,
                       video_id: str,
                       note: str | None = ...,
                       errnote: str | None = ...,
                       transform_source: Any = ...,
                       fatal: bool = ...,
                       encoding: str | None = ...,
                       data: Any = ...,
                       headers: Mapping[str, str] = ...,
                       query: Mapping[str, str] = ...,
                       expected_status: int | None = ...,
                       impersonate: str | None = ...,
                       require_impersonation: bool = ...) -> Any:
        ...

    def _download_webpage(self,
                          url_or_request: str | urllib.request.Request,
                          video_id: str,
                          note: str | None = ...,
                          errnote: str | None = ...,
                          transform_source: Any = ...,
                          fatal: bool = ...,
                          encoding: str | None = ...,
                          data: Any = ...,
                          headers: Mapping[str, str] = ...,
                          query: Mapping[str, str] = ...,
                          expected_status: int | None = ...,
                          impersonate: str | None = ...,
                          require_impersonation: bool = ...) -> str:
        ...

    def _parse_xml(self,
                   xml_string: str,
                   video_id: str,
                   transform_source: Callable[..., str] | None = ...,
                   fatal: bool = ...,
                   errnote: str | None = ...) -> ET.Element:
        ...

    def _parse_mpd_formats(self,
                           mpd_doc: ET.Element,
                           mpd_id: str | None = ...,
                           mpd_base_url: str = ...,
                           mpd_url: str | None = ...) -> list[Any]:
        ...

    def _real_extract(self, url: str) -> InfoDict:
        ...

    @staticmethod
    def _availability(
        is_private: bool | None = ...,
        needs_premium: bool | None = ...,
        needs_subscription: bool | None = ...,
        needs_auth: bool | None = ...,
        is_unlisted: bool | None = ...
    ) -> Literal['needs_auth', 'premium_only', 'private', 'public', 'subscriber_only',
                 'unlisted'] | None:
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

    def _configuration_arg(self,
                           key: str,
                           default: Any = ...,
                           *,
                           ie_key: str | None = ...,
                           casesense: bool = ...) -> Any:
        ...

    @staticmethod
    def playlist_result(entries: Iterable[InfoDict],
                        playlist_id: str | None = ...,
                        playlist_title: str | None = ...,
                        playlist_description: str | None = ...,
                        *,
                        multi_video: bool = ...,
                        **kwargs: Any) -> InfoDict:
        ...

    def write_debug(self, msg: str, *args: Any, **kwargs: Any) -> None:
        ...
