from collections.abc import Sequence
from typing import Any, Self

from . import YDLOpts
from .extractor.common import InfoExtractor

__all__ = ('YoutubeDL',)


class YoutubeDL:
    def __init__(self, options: YDLOpts) -> None:
        ...

    def __enter__(self) -> Self:
        ...

    def __exit__(self, *args: object) -> None:
        ...

    def download(self, urls: Sequence[str]) -> None:
        ...

    def add_info_extractor(self, ie: InfoExtractor) -> None:
        ...

    def extract_info(self, url: str) -> Any:
        ...
