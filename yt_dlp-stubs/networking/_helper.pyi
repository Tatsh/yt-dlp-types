from collections.abc import Callable

from .common import Request, RequestHandler, Response

def wrap_request_errors(
    func: Callable[[RequestHandler, Request], Response | None],
) -> Callable[[RequestHandler, Request], None]: ...
