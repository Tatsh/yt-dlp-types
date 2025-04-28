from typing import Protocol

from .YoutubeDL import YoutubeDL


class LoggerProtocol(Protocol):
    def __init__(self, ydl: YoutubeDL | None = None) -> None:
        ...

    def debug(self, message: str) -> None:
        ...

    def info(self, message: str) -> None:
        ...

    def warning(self, message: str, *, once: bool = ..., only_once: bool = ...) -> None:
        ...

    def error(self, message: str) -> None:
        ...

    def stdout(self, message: str) -> None:
        ...

    def stderr(self, message: str) -> None:
        ...
