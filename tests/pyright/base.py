# Based on https://github.com/sbdchd/django-types/blob/main/tests/pyright/base.py
from os.path import abspath, dirname
from typing import Literal, Sequence, TypedDict, cast
import json
import subprocess as sp
import tempfile

ResultType = Literal['error', 'information']

CWD = dirname(dirname(dirname(abspath(__file__))))


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
    generalDiagnostics: Sequence[GeneralDiagnostics]  # pylint: disable=invalid-name


def run_pyright(code: str) -> Result:
    with tempfile.NamedTemporaryFile('w', suffix='.py') as f:
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
