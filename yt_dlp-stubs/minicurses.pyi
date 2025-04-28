from typing import Any, Self, TextIO
from collections.abc import Callable

CONTROL_SEQUENCES: dict[str, str] = ...


def format_text(text: str, f: str) -> str:
    ...


class MultilinePrinterBase:
    def __init__(self, stream: TextIO = ..., lines: int = ...) -> None:
        ...

    def __enter__(self) -> Self:
        ...

    def __exit__(self, *args: object) -> None:
        ...

    def print_at_line(self, text: str, pos: int) -> None:
        ...

    def end(self) -> None:
        ...

    def write(self, *text: str) -> None:
        ...


class QuietMultilinePrinter(MultilinePrinterBase):
    ...


class MultilineLogger(MultilinePrinterBase):
    ...


class BreaklineStatusPrinter(MultilinePrinterBase):
    ...


class MultilinePrinter(MultilinePrinterBase):
    def __init__(self,
                 stream: TextIO | None = ...,
                 lines: int = ...,
                 preserve_output: bool = ...) -> None:
        ...

    def lock(func: Callable[..., Any]) -> Callable[..., Any]:
        ...
