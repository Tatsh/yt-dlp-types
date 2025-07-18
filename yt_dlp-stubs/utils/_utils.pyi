import enum
import html.parser
import json
import netrc
import subprocess
import sys
import types
from _typeshed import (
    ExcInfo,
    FileDescriptorLike,
    FileDescriptorOrPath,
    OpenBinaryMode,
    OpenTextMode,
    ReadableBuffer,
    StrOrBytesPath,  # noqa: PLC2701
    Unused,
)
from collections import deque
from collections.abc import Callable, Collection, Hashable, Iterable, Iterator, Mapping, Sequence
from datetime import date, datetime, timedelta
from functools import cache
from optparse import Values
from os import PathLike
from re import Pattern
from typing import IO, Any, AnyStr, BinaryIO, Generic, NamedTuple, TextIO, TypeVar, overload
from typing_extensions import Self
from typing import TypeAlias
from xml.etree import ElementTree as ET

from yt_dlp.networking import Response

from .. import _Params
from ..extractor.common import InfoExtractor, _InfoDict
from ..options import _YoutubeDLOptionParser
from ..YoutubeDL import YoutubeDL

_T = TypeVar('_T')


class NO_DEFAULT:
    ...


def IDENTITY(x: _T) -> _T:
    ...


ENGLISH_MONTH_NAMES: Sequence[str]
MONTH_NAMES: Mapping[str, Sequence[str]]
TIMEZONE_NAMES: Mapping[str, str]
ACCENT_CHARS: Mapping[str, str]
DATE_FORMATS: Sequence[str]
DATE_FORMATS_DAY_FIRST: Sequence[str]
DATE_FORMATS_MONTH_FIRST: Sequence[str]
PACKED_CODES_RE: str
JSON_LD_RE: str
NUMBER_RE: str


@cache
def preferredencoding() -> str:
    ...


def write_json_file(obj: Any, fn: str) -> None:
    ...


def partial_application(func: Callable[..., object]) -> Callable[..., object]:
    ...


def find_xpath_attr(node: ET.ElementTree,
                    xpath: str,
                    key: str,
                    val: str | None = None) -> ET.Element | None:
    ...


def xpath_with_ns(path: str, ns_map: Mapping[str, str]) -> str:
    ...


def xpath_element(node: ET.ElementTree,
                  xpath: str,
                  name: str | None = None,
                  fatal: bool = False,
                  default: ET.Element | type[NO_DEFAULT] = ...) -> ET.Element | None:
    ...


def xpath_text(node: ET.ElementTree,
               xpath: str,
               name: str | None = None,
               fatal: bool = False,
               default: str | type[NO_DEFAULT] = ...) -> str | None:
    ...


def xpath_attr(
    node: ET.ElementTree,
    xpath: str,
    key: str,
    name: str | None = None,
    fatal: bool = False,
    default: str | type[NO_DEFAULT] = ...,
) -> str | None:
    ...


def get_element_by_id(id: str, html: str, **kwargs: object) -> str | None:
    ...


def get_element_html_by_id(id: str, html: str, **kwargs: object) -> str | None:
    ...


def get_element_by_class(class_name: str, html: str) -> str:
    ...


def get_element_html_by_class(class_name: str, html: str) -> str:
    ...


def get_element_by_attribute(attribute: str, value: str, html: str, **kwargs: object) -> str:
    ...


def get_element_html_by_attribute(attribute: str, value: str, html: str,
                                  **kargs: object) -> list[str]:
    ...


def get_elements_by_class(class_name: str, html: str, **kargs: object) -> list[str]:
    ...


def get_elements_html_by_class(class_name: str, html: str) -> list[str]:
    ...


def get_elements_by_attribute(*args: object, **kwargs: object) -> list[str]:
    ...


def get_elements_html_by_attribute(*args: object, **kwargs: object) -> list[str]:
    ...


def get_elements_text_and_html_by_attribute(attribute: str,
                                            value: str,
                                            html: str,
                                            *,
                                            tag: str = '[\\w:.-]+',
                                            escape_value: bool = True) -> Iterator[str]:
    ...


class HTMLBreakOnClosingTagParser(html.parser.HTMLParser):
    class HTMLBreakOnClosingTagException(Exception):
        ...

    tagstack: deque[object]

    def __init__(self) -> None:
        ...

    def __enter__(self) -> Self:
        ...

    def __exit__(self, *_: object) -> None:
        ...

    def close(self) -> None:
        ...

    def handle_starttag(self, tag: str, _: object) -> None:
        ...

    def handle_endtag(self, tag: str) -> None:
        ...


def get_element_text_and_html_by_tag(tag: str, html: str) -> str:
    ...


class HTMLAttributeParser(html.parser.HTMLParser):
    attrs: dict[str, str | None]

    def __init__(self) -> None:
        ...

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        ...


class HTMLListAttrsParser(html.parser.HTMLParser):
    items: list[dict[str, str | None]]

    def __init__(self) -> None:
        ...

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        ...

    def handle_endtag(self, tag: str) -> None:
        ...


def extract_attributes(html_element: str) -> dict[str, str]:
    ...


def parse_list(webpage: str) -> list[dict[str, str | None]]:
    ...


def clean_html(html: str | None) -> str | None:
    ...


class LenientJSONDecoder(json.JSONDecoder):
    def __init__(
        self,
        *args: object,
        transform_source: Callable[[str], str] | None = None,
        ignore_extra: bool = False,
        close_objects: int = 0,
        **kwargs: object,
    ) -> None:
        ...

    def decode(self, s: str) -> Any:  # type: ignore[override]
        ...


@overload
def sanitize_open(filename: FileDescriptorOrPath, open_mode: OpenBinaryMode) -> BinaryIO:
    ...


@overload
def sanitize_open(filename: FileDescriptorOrPath, open_mode: OpenTextMode) -> TextIO:
    ...


def timeconvert(timestr: str) -> str:
    ...


def sanitize_filename(s: str,
                      restricted: bool = False,
                      is_id: bool | type[NO_DEFAULT] = ...) -> str:
    ...


def sanitize_path(s: str, force: bool = False) -> str:
    ...


def sanitize_url(url: str, *, scheme: str = 'http') -> str:
    ...


def extract_basic_auth(url: str) -> tuple[str, str | None]:
    ...


def expand_path(s: str) -> str:
    ...


def orderedSet(iterable: Iterable[_T], *, lazy: bool = False) -> Iterator[_T]:
    ...


def unescapeHTML(s: str | None) -> str | None:
    ...


def escapeHTML(text: str) -> str:
    ...


class netrc_from_content(netrc.netrc):
    def __init__(self, content: str) -> None:
        ...


def encodeArgument(s: str) -> str:
    ...


class _timetuple(NamedTuple):
    hours: tuple[int, int]
    minutes: tuple[int, int]
    seconds: tuple[int, int]
    milliseconds: tuple[int, int]


def timetuple_from_msec(msec: int) -> _timetuple:
    ...


def formatSeconds(secs: int, delim: str = ':', msec: bool = False) -> str:
    ...


def bug_reports_message(before: str = ';') -> None:
    ...


class YoutubeDLError(Exception):
    msg: str | None

    def __init__(self, msg: str | None = None) -> None:
        ...


class ExtractorError(YoutubeDLError):
    orig_msg: object
    traceback: types.TracebackType | None
    expected: object
    cause: object
    video_id: str
    ie: InfoExtractor
    exc_info: ExcInfo

    def __init__(
        self,
        msg: str,
        tb: types.TracebackType | None = None,
        expected: bool = False,
        cause: object | None = None,
        video_id: str | None = None,
        ie: InfoExtractor | None = None,
    ) -> None:
        ...

    def format_traceback(self) -> str:
        ...

    msg: str | None
    args: tuple[object, ...]

    def __setattr__(self, name: str, value: object) -> None:
        ...


class UnsupportedError(ExtractorError):
    url: str

    def __init__(self, url: str) -> None:
        ...


class RegexNotFoundError(ExtractorError):
    ...


class GeoRestrictedError(ExtractorError):
    countries: str | None

    def __init__(self, msg: str, countries: str | None = None, **kwargs: object) -> None:
        ...


class UserNotLive(ExtractorError):
    def __init__(self, msg: str | None = None, **kwargs: object) -> None:
        ...


class DownloadError(YoutubeDLError):
    exc_info: ExcInfo

    def __init__(self, msg: str, exc_info: ExcInfo | None = None) -> None:
        ...


class EntryNotInPlaylist(YoutubeDLError):
    msg: str


class SameFileError(YoutubeDLError):
    msg: str

    def __init__(self, filename: str | None = None) -> None:
        ...


class PostProcessingError(YoutubeDLError):
    ...


class DownloadCancelled(YoutubeDLError):
    msg: str


class ExistingVideoReached(DownloadCancelled):
    msg: str


class RejectedVideoReached(DownloadCancelled):
    msg: str


class MaxDownloadsReached(DownloadCancelled):
    msg: str


class ReExtractInfo(YoutubeDLError):
    expected: bool

    def __init__(self, msg: str, expected: bool = False) -> None:
        ...


class ThrottledDownload(ReExtractInfo):
    msg: str

    def __init__(self) -> None:
        ...


class UnavailableVideoError(YoutubeDLError):
    msg: str

    def __init__(self, err: str | None = None) -> None:
        ...


class ContentTooShortError(YoutubeDLError):
    downloaded: int
    expected: int

    def __init__(self, downloaded: int, expected: int) -> None:
        ...


class XAttrMetadataError(YoutubeDLError):
    code: str | None
    msg: str | None
    reason: str

    def __init__(self, code: str | None = None, msg: str = 'Unknown error') -> None:
        ...


class XAttrUnavailableError(YoutubeDLError):
    ...


def is_path_like(f: object) -> bool:
    ...


def extract_timezone(date_str: str,
                     default: type[NO_DEFAULT] | object | None = None) -> tuple[timedelta, str]:
    ...


def parse_iso8601(date_str: str,
                  delimiter: str = 'T',
                  timezone: type[NO_DEFAULT] | object | None = None) -> int:
    ...


def date_formats(day_first: bool = True) -> list[str]:
    ...


def unified_strdate(date_str: str, day_first: bool = True) -> str:
    ...


def unified_timestamp(date_str: str, day_first: bool = True) -> int:
    ...


def determine_ext(url: str, default_ext: str = 'unknown_video') -> str:
    ...


def subtitles_filename(filename: str,
                       sub_lang: str,
                       sub_format: str,
                       expected_real_ext: str | None = None) -> str:
    ...


def datetime_from_str(date_str: str, precision: str = 'auto', format: str = '%Y%m%d') -> datetime:
    ...


def date_from_str(date_str: str, format: str = '%Y%m%d', strict: bool = False) -> date:
    ...


def datetime_add_months(dt_: datetime, months: int) -> datetime:
    ...


def datetime_round(dt_: datetime, precision: str = 'day') -> datetime:
    ...


def hyphenate_date(date_str: str) -> str:
    ...


class DateRange:
    start: date
    end: date

    def __init__(self, start: date | None = None, end: date | None = None) -> None:
        ...

    @classmethod
    def day(cls, day: date) -> Self:
        ...

    def __contains__(self, date: date) -> bool:
        ...

    def __eq__(self, other: object) -> bool:
        ...


def system_identifier() -> str:
    ...


def get_windows_version() -> tuple[str, ...]:
    ...


def write_string(s: str, out: TextIO | None = None, encoding: str | None = None) -> None:
    ...


def deprecation_warning(msg: str,
                        *,
                        printer: Callable[..., object] | None = None,
                        stacklevel: int = 0,
                        **kwargs: object) -> None:
    ...


class LockingUnsupportedError(OSError):
    msg: str

    def __init__(self) -> None:
        ...


class locked_file:
    locked: bool
    f: TextIO

    def __init__(self,
                 filename: AnyStr,
                 mode: OpenTextMode | OpenBinaryMode,
                 block: bool = True,
                 encoding: str | None = None) -> None:
        ...

    def __enter__(self) -> Self:
        ...

    def unlock(self) -> None:
        ...

    def __exit__(self, *_: object) -> None:
        ...

    open = __enter__
    close = __exit__

    def __getattr__(self, attr: str) -> object:
        ...

    def __iter__(self) -> str:
        ...


def get_filesystem_encoding() -> str:
    ...


def shell_quote(args: str | Collection[str], *, shell: bool = False) -> str:
    ...


def smuggle_url(url: str, data: object) -> str:
    ...


def unsmuggle_url(smug_url: str, default: object | None = None) -> tuple[str, object]:
    ...


def format_decimal_suffix(num: float, fmt: str = '%d%s', *, factor: int = 1000) -> str:
    ...


def format_bytes(bytes: int) -> str:
    ...


def lookup_unit_table(unit_table: Mapping[str, int], s: str, strict: bool = False) -> float:
    ...


def parse_bytes(s: str) -> int:
    ...


def parse_filesize(s: str | None) -> int | None:
    ...


def parse_count(s: str | None) -> str | None:
    ...


def parse_resolution(s: str, *, lenient: bool = False) -> dict[str, int]:
    ...


def parse_bitrate(s: str) -> int:
    ...


def month_by_name(name: str, lang: str = 'en') -> str | None:
    ...


def month_by_abbreviation(abbrev: str) -> str | None:
    ...


def fix_xml_ampersands(xml_str: str) -> str:
    ...


def setproctitle(title: str) -> None:
    ...


def remove_start(s: str, start: str) -> str:
    ...


def remove_end(s: str, end: str) -> str:
    ...


def remove_quotes(s: str) -> str:
    ...


def get_domain(url: str) -> str | None:
    ...


def url_basename(url: str) -> str:
    ...


def base_url(url: str) -> str:
    ...


def urljoin(base: str, path: str) -> str:
    ...


def int_or_none(v: object,
                scale: int = 1,
                default: int | None = None,
                get_attr: str | None = None,
                invscale: int = 1,
                base: int | None = None) -> int | None:
    ...


def str_or_none(v: object, default: str | None = None) -> str:
    ...


def str_to_int(int_str: str) -> int:
    ...


def float_or_none(v: object,
                  scale: int = 1,
                  invscale: int = 1,
                  default: float | None = None) -> float | None:
    ...


def bool_or_none(v: object, default: bool | None = None) -> bool | None:
    ...


def strip_or_none(v: object, default: str | None = None) -> str | None:
    ...


def url_or_none(url: object) -> str | None:
    ...


def strftime_or_none(timestamp: int,
                     date_format: str = '%Y%m%d',
                     default: str | None = None) -> str | None:
    ...


def parse_duration(s: str | None) -> float:
    ...


def prepend_extension(filename: str, ext: str, expected_real_ext: str | None = None) -> str:
    ...


def replace_extension(filename: str, ext: str, expected_real_ext: str | None = None) -> str:
    ...


def check_executable(exe: str, args: Iterable[str] = ...) -> str | None:
    ...


def detect_exe_version(output: str,
                       version_re: str | Pattern[str] | None = None,
                       unrecognized: str = 'present') -> str:
    ...


def get_exe_version(
        exe: str,
        args: Iterable[str] = ['--version'],
        version_re: str | None = None,
        unrecognized: Iterable[str] = ('present', 'broken'),
) -> str:
    ...


def frange(start: int = 0, stop: int | None = None, step: int = 1) -> Iterator[float]:
    ...


class LazyList(Sequence[_T]):
    def __init__(self,
                 iterable: Iterable[_T],
                 *,
                 reverse: bool = False,
                 _cache: list[object] | None = None) -> None:
        ...

    def __iter__(self) -> Iterator[_T]:
        ...

    def exhaust(self) -> list[_T]:
        ...

    @overload
    def __getitem__(self, idx: int, /) -> _T:
        ...

    @overload
    def __getitem__(self, idx: slice, /) -> list[_T]:
        ...

    def __bool__(self) -> bool:
        ...

    def __len__(self) -> int:
        ...

    def __reversed__(self) -> Iterator[_T]:
        ...

    def __copy__(self) -> Self:
        ...


class PagedList:
    def __len__(self) -> int:
        ...

    def __init__(self,
                 pagefunc: Callable[[int], Iterator[object]],
                 pagesize: int,
                 use_cache: bool = True) -> None:
        ...

    def getpage(self, pagenum: int) -> list[object]:
        ...

    def getslice(self, start: int = 0, end: int | None = None) -> list[object]:
        ...

    @overload
    def __getitem__(self, idx: int, /) -> object:
        ...

    @overload
    def __getitem__(self, idx: slice, /) -> list[object]:
        ...

    def __bool__(self) -> bool:
        ...


class OnDemandPagedList(PagedList):
    ...


class InAdvancePagedList(PagedList):
    def __init__(self, pagefunc: Callable[[int], Iterator[object]], pagecount: int,
                 pagesize: int) -> None:
        ...


class PlaylistEntries:
    MissingEntry: object
    is_exhausted: bool
    ydl: YoutubeDL
    is_incomplete: bool

    def __init__(self, ydl: YoutubeDL, info_dict: _InfoDict) -> None:
        ...

    PLAYLIST_ITEMS_RE: Pattern[str]

    @classmethod
    def parse_playlist_items(cls, string: str) -> slice | int:
        ...

    def get_requested_items(self) -> Iterator[tuple[int, object]]:
        ...

    def get_full_count(self) -> int | None:
        ...

    def __getitem__(self, idx: int) -> Iterator[tuple[int, object]]:
        ...

    def __len__(self) -> int:
        ...


_K = TypeVar('_K')
_V = TypeVar('_V')


def uppercase_escape(s: str) -> str:
    ...


def lowercase_escape(s: str) -> str:
    ...


def parse_qs(url: str, **kwargs: object) -> dict[AnyStr, list[AnyStr]]:
    ...


def read_batch_urls(batch_fd: FileDescriptorLike) -> list[str]:
    ...


def urlencode_postdata(*args: object, **kargs: object) -> bytes:
    ...


def update_url(url: str, *, query_update: Mapping[str, str] | None = None, **kwargs: object) -> str:
    ...


def update_url_query(url: str, query: Mapping[str, str]) -> str:
    ...


def multipart_encode(data: Mapping[AnyStr, AnyStr],
                     boundary: str | None = None) -> tuple[bytes, str]:
    ...


def is_iterable_like(x: object,
                     allowed_types: Collection[type[Any]] = ...,
                     blocked_types: Collection[type[Any]] | type[NO_DEFAULT] = ...) -> bool:
    ...


def variadic(x: _T,
             allowed_types: Collection[type[Any]] | type[NO_DEFAULT] = ...) -> _T | tuple[_T]:
    ...


def try_call(
    *funcs: Callable[..., _T],
    expected_type: type[_T] | None = None,
    args: Iterable[object] = ...,
    kwargs: Mapping[Hashable, object] = ...,
) -> _T | None:
    ...


def try_get(src: object,
            getter: Callable[..., _T] | Collection[Callable[..., _T]],
            expected_type: type[_T] | None = None) -> _T:
    ...


def filter_dict(dct: Mapping[_K, _V], cndn: Callable[[_K, _V], bool] = ...) -> dict[_K, _V]:
    ...


def merge_dicts(*dicts: Mapping[Hashable, object]) -> dict[Hashable, object]:
    ...


def encode_compat_str(string: str, encoding: str = ..., errors: str = 'strict') -> str:
    ...


US_RATINGS: Mapping[str, int]
TV_PARENTAL_GUIDELINES: Mapping[str, int]


def parse_age_limit(s: int) -> int | None:
    ...


def strip_jsonp(code: str) -> str:
    ...


def js_to_json(code: str, vars: Mapping[str, object] = ..., *, strict: bool = False) -> str:
    ...


def qualities(quality_ids: Sequence[int]) -> Callable[[int], int]:
    ...


POSTPROCESS_WHEN: tuple[str, ...]
DEFAULT_OUTTMPL: Mapping[str, str]
OUTTMPL_TYPES: Mapping[str, str | None]
STR_FORMAT_RE_TMPL: str
STR_FORMAT_TYPES: str


def limit_length(s: str, length: int) -> str:
    ...


def version_tuple(v: str) -> tuple[int, ...]:
    ...


def is_outdated_version(version: str, limit: str, assume_new: bool = True) -> bool:
    ...


def ytdl_is_updateable() -> bool:
    ...


def args_to_str(args: str | Collection[str]) -> str:
    ...


def error_to_str(err: BaseException) -> str:
    ...


def mimetype2ext(mt: str, default: str | type[NO_DEFAULT] = ...) -> str:
    ...


def ext2mimetype(ext_or_url: str | None) -> str:
    ...


def parse_codecs(codecs_str: str) -> dict[str, str]:
    ...


def get_compatible_ext(
    *,
    vcodecs: Collection[str],
    acodecs: Collection[str],
    vexts: Collection[str],
    aexts: Collection[str],
    preferences: Sequence[str] | None = None,
) -> str:
    ...


def urlhandle_detect_ext(url_handle: Response, default: str | type[NO_DEFAULT] = ...) -> str | None:
    ...


def encode_data_uri(data: ReadableBuffer, mime_type: str) -> str:
    ...


def age_restricted(content_limit: int | None, age_limit: int | None) -> bool:
    ...


BOMS: Collection[tuple[bytes, str]]


def is_html(first_bytes: bytes) -> bool:
    ...


def determine_protocol(info_dict: _InfoDict) -> str:
    ...


def render_table(header_row: Iterable[str],
                 data: Iterable[str],
                 delim: bool = False,
                 extra_gap: int = 0,
                 hide_empty: bool = False) -> str:
    ...


def match_str(filter_str: str, dct: Mapping[str, object], incomplete: bool = False) -> bool:
    ...


def match_filter_func(
    filters: Collection[str] | str,
    breaking_filters: Collection[str] | str | None = None
) -> Callable[..., str | type[NO_DEFAULT] | None]:
    ...


class download_range_func:
    def __init__(self,
                 chapters: Iterable[str | Pattern[str]],
                 ranges: Iterable[tuple[int, int]],
                 from_info: bool = False) -> None:
        ...

    def __call__(self, info_dict: _InfoDict, ydl: YoutubeDL) -> Iterator[dict[str, object]]:
        ...

    def __eq__(self, other: object) -> bool:
        ...


def parse_dfxp_time_expr(time_expr: str | None) -> int | None:
    ...


def srt_subtitles_timecode(seconds: float) -> str:
    ...


def ass_subtitles_timecode(seconds: float) -> str:
    ...


def dfxp2srt(dfxp_data: bytes) -> str:
    ...


def cli_option(params: _Params,
               command_option: str,
               param: str,
               separator: str | None = None) -> object:
    ...


def cli_bool_option(
    params: _Params,
    command_option: str,
    param: bool | None,
    true_value: str = 'true',
    false_value: str = 'false',
    separator: str | None = None,
) -> object:
    ...


def cli_valueless_option(params: _Params,
                         command_option: str,
                         param: str,
                         expected_value: bool = True) -> object:
    ...


def cli_configuration_args(argdict: dict[str, object],
                           keys: Iterable[str],
                           default: object = ...,
                           use_compat: bool = True) -> object:
    ...


class ISO639Utils:
    @classmethod
    def short2long(cls, code: str) -> str | None:
        ...

    @classmethod
    def long2short(cls, code: str) -> str | None:
        ...


class ISO3166Utils:
    @classmethod
    def short2full(cls, code: str) -> str | None:
        ...


class GeoUtils:
    @classmethod
    def random_ipv4(cls, code_or_block: str) -> str | None:
        ...


def long_to_bytes(n: int, blocksize: int = 0) -> bytes:
    ...


def bytes_to_long(s: bytes) -> int:
    ...


def ohdave_rsa_encrypt(data: ReadableBuffer, exponent: float, modulus: float | None) -> str:
    ...


def pkcs1pad(data: Sequence[int], length: int) -> list[int]:
    ...


def encode_base_n(num: int, n: int | None = None, table: str | None = None) -> str:
    ...


def decode_base_n(string: str, n: int | None = None, table: str | None = None) -> int:
    ...


def decode_packed_codes(code: str) -> str:
    ...


def caesar(s: str, alphabet: str, shift: int) -> str:
    ...


def rot47(s: str) -> str:
    ...


def parse_m3u8_attributes(attrib: str) -> dict[str, str]:
    ...


def urshift(val: int, n: int) -> int:
    ...


def write_xattr(path: FileDescriptorOrPath, key: str, value: str) -> None:
    ...


def random_birthday(year_field: Hashable, month_field: Hashable,
                    day_field: Hashable) -> dict[Hashable, str]:
    ...


def find_available_port(interface: str = '') -> object | None:
    ...


DOT_URL_LINK_TEMPLATE: str
DOT_WEBLOC_LINK_TEMPLATE: str
DOT_DESKTOP_LINK_TEMPLATE: str
LINK_TEMPLATES: Mapping[str, str]


def iri_to_uri(iri: str) -> str:
    ...


def to_high_limit_path(path: PathLike[AnyStr]) -> str:
    ...


def format_field(
    obj: object,
    field: str | Collection[str] | None = None,
    template: str = '%s',
    ignore: type[NO_DEFAULT] | str | Collection[str] = ...,
    default: str = '',
    func: Callable[[object], object] = ...,
) -> str:
    ...


def clean_podcast_url(url: str) -> str:
    ...


def random_uuidv4() -> str:
    ...


def make_dir(path: PathLike[AnyStr], to_screen: Callable[[str], object] | None = None) -> bool:
    ...


def get_executable_path() -> str:
    ...


def get_user_config_dirs(package_name: str) -> Iterator[str]:
    ...


def get_system_config_dirs(package_name: str) -> Iterator[str]:
    ...


def time_seconds(**kwargs: float) -> int:
    ...


def jwt_encode_hs256(payload_data: object, key: str, headers: Mapping[str, object] = ...) -> bytes:
    ...


def jwt_decode_hs256(jwt: str) -> object:
    ...


WINDOWS_VT_MODE: bool | None


def supports_terminal_sequences(stream: IO[Any]) -> bool:
    ...


def windows_enable_vt_mode() -> None:
    ...


def remove_terminal_sequences(string: str) -> str:
    ...


def number_of_digits(number: int) -> int:
    ...


def join_nonempty(*values: str,
                  delim: str = '-',
                  from_dict: Mapping[str, object] | None = None) -> str:
    ...


def scale_thumbnails_to_max_format_width(
        formats: Iterable[Mapping[str, object]], thumbnails: Iterable[Mapping[str, object]],
        url_width_re: str | Pattern[str]) -> list[dict[str, object]]:
    ...


def parse_http_range(range: str | None) -> tuple[int | None, int | None, int | None]:
    ...


def read_stdin(what: str) -> TextIO | object:
    ...


def determine_file_encoding(data: bytes) -> tuple[str | None, int]:
    ...


class Config:
    own_args: object | None
    parsed_args: tuple[Values, list[str]] | None
    filename: str | None

    def __init__(self, parser: _YoutubeDLOptionParser, label: str | None = None) -> None:
        ...

    def init(self, args: object | None = None, filename: str | None = None) -> bool:
        ...

    def load_configs(self) -> bool:
        ...

    @staticmethod
    def read_file(filename: FileDescriptorOrPath, default: list[str] = []) -> list[str]:
        ...

    @staticmethod
    def hide_login_info(opts: Iterable[str]) -> list[str]:
        ...

    def append_config(self, *args: object, label: str | None = None) -> None:
        ...

    @property
    def all_args(self) -> Iterator[str]:
        ...

    def parse_known_args(self, **kwargs: object) -> tuple[Values, list[str]]:
        ...

    def parse_args(self) -> tuple[Values, list[str]]:
        ...


def merge_headers(*dicts: dict[str, object]) -> dict[str, object]:
    ...


def cached_method(f: Callable[..., object]) -> Callable[..., object]:
    ...


class function_with_repr(Generic[_T]):
    def __init__(self, func: Callable[..., _T], repr_: str | None = None) -> None:
        ...

    def __call__(self, *args: object, **kwargs: object) -> _T:
        ...

    @classmethod
    def set_repr(cls, repr_: str) -> Callable[..., object]:
        ...


class Namespace(types.SimpleNamespace):
    def __iter__(self) -> Iterator[object]:
        ...

    @property
    def items_(self) -> dict[str, object]:
        ...


MEDIA_EXTENSIONS: Namespace
KNOWN_EXTENSIONS: tuple[str, ...]


class _UnsafeExtensionError(Exception):
    ALLOWED_EXTENSIONS: frozenset[str]
    extension: str

    def __init__(self, extension: str, /) -> None:
        ...

    @classmethod
    def sanitize_extension(cls, extension: str, /, *, prepend: bool = False) -> str:
        ...


class RetryManager:
    attempt: int
    retries: int
    error_callback: Callable[[BaseException, int, int], object]

    def __init__(self, _retries: int | None, _error_callback: Callable[..., object],
                 **kwargs: object) -> None:
        ...

    @property
    def error(self) -> None:
        ...

    @error.setter
    def error(self, value: type[NO_DEFAULT] | BaseException) -> None:
        ...

    def __iter__(self) -> Self:
        ...

    @staticmethod
    def report_retry(
        e: BaseException,
        count: int,
        retries: int,
        *,
        sleep_func: Callable[..., float | None],
        info: Callable[[str], object],
        warn: Callable[[str], object],
        error: Callable[[str], object] | None = None,
        suffix: str | None = None,
    ) -> None:
        ...


def make_archive_id(ie: InfoExtractor, video_id: str) -> str:
    ...


def truncate_string(s: str, left: int, right: int = 0) -> str:
    ...


def orderedSet_from_options(
    options: Sequence[str],
    alias_dict: dict[str, Sequence[str]],
    *,
    use_regex: bool = False,
    start: Iterable[object] | None = None,
) -> Iterator[object]:
    ...


class FormatSorter:
    regex: str
    default: tuple[str, ...]
    ytdl_default: tuple[str, ...]
    settings: dict[str, object]
    ydl: YoutubeDL

    def __init__(self, ydl: YoutubeDL, field_preference: _Params) -> None:
        ...

    def evaluate_params(self, params: _Params, sort_extractor: Collection[str]) -> None:
        ...

    def print_verbose_info(self, write_debug: Callable[..., None]) -> None:
        ...

    def calculate_preference(self, format: dict[str, object]) -> tuple[int, ...]:
        ...


@overload
def filesize_from_tbr(tbr: None, duration: None) -> None:
    ...


@overload
def filesize_from_tbr(tbr: int, duration: None) -> None:
    ...


@overload
def filesize_from_tbr(tbr: None, duration: int) -> None:
    ...


@overload
def filesize_from_tbr(tbr: int | None, duration: int | None) -> int | None:
    ...


class _YDLLogger:
    def __init__(self, ydl: YoutubeDL | None = None) -> None:
        ...

    def debug(self, message: str) -> None:
        ...

    def info(self, message: str) -> None:
        ...

    def warning(self, message: str, *, once: bool = False) -> None:
        ...

    def error(self, message: str, *, is_error: bool = True) -> None:
        ...

    def stdout(self, message: str) -> None:
        ...

    def stderr(self, message: str) -> None:
        ...


class _ProgressState(enum.Enum):
    HIDDEN = 0
    INDETERMINATE = 3
    VISIBLE = 1
    WARNING = 4
    ERROR = 2

    @classmethod
    def from_dict(cls, s: dict[str, object], /) -> _ProgressState:
        ...

    def get_ansi_escape(self, /, percent: int | None = None) -> str:
        ...


if sys.platform == 'win32':
    _ENV: TypeAlias = Mapping[str, str]
else:
    _ENV: TypeAlias = Mapping[bytes, StrOrBytesPath] | Mapping[str, StrOrBytesPath]


class Popen(subprocess.Popen[AnyStr]):
    def __init__(
        self,
        args: StrOrBytesPath | Sequence[StrOrBytesPath],
        *remaining: object,
        env: _ENV | None = None,
        text: bool = False,
        shell: bool = False,
        **kwargs: object,
    ) -> None:
        ...

    def communicate_or_kill(self, *args: object, **kwargs: object) -> tuple[AnyStr, AnyStr]:
        ...

    def kill(self, *, timeout: int = 0) -> None:
        ...

    @classmethod
    def run(cls,
            *args: object,
            timeout: int | None = None,
            **kwargs: object) -> tuple[AnyStr, AnyStr]:
        ...


class classproperty:
    def __new__(cls,
                func: Callable[..., object] | None = None,
                *args: object,
                **kwargs: object) -> Self:
        ...

    def __init__(  # pyright: ignore[reportInconsistentConstructor]
            self,
            func: Callable[..., object],
            *,
            cache: bool = False) -> None:
        ...

    def __get__(self, _: Unused, cls: type[object]) -> object:
        ...
