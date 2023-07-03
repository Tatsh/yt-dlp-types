from typing import Any, Sequence

from . import YDLOpts
from .extractor.common import InfoExtractor

__all__ = ('YoutubeDL',)


class YoutubeDL:
    def __init__(self, options: YDLOpts) -> None:
        ...

    def __enter__(self) -> YoutubeDL:
        ...

    def __exit__(self, *args: Any) -> None:
        ...

    def download(self, urls: Sequence[str]) -> None:
        ...

    def add_info_extractor(self, ie: InfoExtractor) -> None:
        ...

    def extract_info(self, url: str) -> Any:
        ...
