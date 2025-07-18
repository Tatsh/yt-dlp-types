from _typeshed import StrPath
from collections.abc import Callable
from typing import Any

from ..extractor.common import _InfoDict
from ..YoutubeDL import YoutubeDL


class PostProcessorMetaClass(type):
    @staticmethod
    def run_wrapper(func: Callable[..., object]) -> Callable[..., object]:
        ...

    def __new__(cls, name: str, bases: tuple[type[Any], ...], attrs: dict[str,
                                                                          object]) -> type[Any]:
        ...


class PostProcessor(metaclass=PostProcessorMetaClass):
    PP_NAME: str

    def __init__(self, downloader: YoutubeDL | None = None) -> None:
        ...

    @classmethod
    def pp_key(cls) -> str:
        ...

    def to_screen(self, text: str, prefix: bool = True, *args: object, **kwargs: object) -> None:
        ...

    def report_warning(self, text: str, *args: object, **kwargs: object) -> None:
        ...

    def deprecation_warning(self, msg: str) -> None:
        ...

    def deprecated_feature(self, msg: str) -> None:
        ...

    def write_debug(self, text: str, *args: object, **kwargs: object) -> None:
        ...

    def get_param(self,
                  name: str,
                  default: object | None = None,
                  *args: object,
                  **kwargs: object) -> object:
        ...

    def set_downloader(self, downloader: YoutubeDL) -> None:
        ...

    def run(self, information: _InfoDict) -> tuple[list[str], _InfoDict]:
        ...

    def try_utime(self,
                  path: StrPath,
                  atime: int,
                  mtime: int,
                  errnote: str = 'Cannot update utime of file') -> None:
        ...

    def add_progress_hook(self, ph: Callable[[str], object]) -> None:
        ...

    def report_progress(self, s: str) -> None:
        ...
