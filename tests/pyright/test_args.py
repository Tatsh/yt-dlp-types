from .base import run_pyright


def test_download_json() -> None:
    results = run_pyright('''
from typing import Any
from yt_dlp.extractor.common import InfoExtractor


class MyIE(InfoExtractor):
    def _real_extract(self, url: str) -> Any:
        self._download_json(1, 2)
''')['generalDiagnostics']
    assert results[0]['message'].startswith(
        'Argument of type "Literal[1]" cannot be assigned to parameter "url" of type '
        '"str | Request" in function "_download_json"')
    assert results[1]['message'].startswith(
        'Argument of type "Literal[2]" cannot be assigned to parameter "video_id" of type "str" in '
        'function "_download_json"')


def test_availability() -> None:
    results = run_pyright('''
from typing import Any
from yt_dlp.extractor.common import InfoExtractor


class MyIE(InfoExtractor):
    def _real_extract(self, url: str) -> Any:
        self._availability(is_private=1)
''')['generalDiagnostics']
    assert results[0]['message'].startswith(
        'Argument of type "Literal[1]" cannot be assigned to parameter "is_private" of type '
        '"bool | None"')
