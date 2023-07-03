from typing import Sequence

from . import YDLOpts
from .extractor.common import InfoExtractor

__all__ = ('YoutubeDL',)


class YoutubeDL:
    def __init__(self, options: YDLOpts) -> None:
        ...

    def __enter__(self) -> YoutubeDL:
        ...

    def __exit__(self) -> None:
        ...

    def download(self, urls: Sequence[str]) -> None:
        ...

    def add_info_extractor(self, ie: InfoExtractor) -> None:
        ...
