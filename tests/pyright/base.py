# Based on https://github.com/sbdchd/django-types/blob/main/tests/pyright/base.py
import json
import subprocess as sp
import tempfile
from collections.abc import Sequence
from pathlib import Path
from typing import Literal, TypedDict, cast

ResultType = Literal['error', 'information']

CWD = str(Path(__file__).absolute().parent.parent.parent)


class RangeField(TypedDict):
    line: int
    character: int


class Range(TypedDict):
    start: RangeField
    end: RangeField


class GeneralDiagnostics(TypedDict):
    severity: Literal['error']
    message: str
    range: Range
    rule: Literal['reportGeneralTypeIssues']


class Result(TypedDict):
    generalDiagnostics: Sequence[GeneralDiagnostics]


def run_pyright(code: str) -> Result:
    with tempfile.NamedTemporaryFile('w', suffix='.py', encoding='utf-8') as f:
        f.write(code)
        f.flush()
        return cast(
            Result,
            json.loads(
                sp.run(('yarn', '-s', 'pyright', '--outputjson', f.name),
                       cwd=CWD,
                       stdout=sp.PIPE,
                       check=False,
                       text=True).stdout))
