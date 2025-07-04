import collections
from collections.abc import Callable, Collection, Mapping
from typing import NoReturn
from typing import TypeAlias

from yt_dlp.utils._utils import function_with_repr

from .utils import ExtractorError


def js_number_to_string(val: float, radix: int = 10) -> str:
    ...


class JS_Undefined:
    ...


class JS_Break(ExtractorError):
    def __init__(self) -> None:
        ...


class JS_Continue(ExtractorError):
    def __init__(self) -> None:
        ...


class JS_Throw(ExtractorError):
    error: BaseException

    def __init__(self, e: BaseException) -> None:
        ...


class LocalNameSpace(collections.ChainMap[str, object]):
    def __setitem__(self, key: str, value: object) -> None:
        ...

    def __delitem__(self, key: str) -> NoReturn:
        ...


class Debugger:
    ENABLED: bool

    @staticmethod
    def write(*args: str, level: int = 100) -> None:
        ...

    @classmethod
    # Callable[[Debugger, str, object, int, ...], tuple[object, bool]] but it also accepts
    # *args, **kwargs.
    def wrap_interpreter(
            cls, f: Callable[..., tuple[object, bool]]) -> Callable[..., tuple[object, bool]]:
        ...


_BuildFunctionReturnType: TypeAlias = Callable[[Collection[object], Mapping[str, object], int],
                                               object | None]


class JSInterpreter:
    def __init__(self, code: str, objects: Mapping[str, object] | None = None) -> None:
        ...

    class Exception(ExtractorError):  # noqa: A001
        def __init__(self,
                     msg: str,
                     expr: str | None = None,
                     *args: object,
                     **kwargs: object) -> None:
            ...

    def interpret_statement(self, stmt: str, local_vars: Mapping[str, object], allow_recursion: int,
                            *args: object, **kwargs: object) -> tuple[object, bool]:
        ...

    def interpret_expression(self, expr: str, local_vars: Mapping[str, object],
                             allow_recursion: int) -> object:
        ...

    def extract_object(self, objname: str, *global_stack: object) -> object:
        ...

    def extract_function_code(self, funcname: str) -> tuple[list[str], tuple[str, str]]:
        ...

    def extract_function(self, funcname: str, *global_stack: object) -> function_with_repr[object]:
        ...

    def extract_function_from_code(self, argnames: Collection[str], code: str, *global_stack:
                                   object) -> _BuildFunctionReturnType:
        ...

    def call_function(self, funcname: str, *args: object) -> function_with_repr[object]:
        ...

    def build_function(self, argnames: Collection[str], code: str, *global_stack:
                       object) -> _BuildFunctionReturnType:
        ...
