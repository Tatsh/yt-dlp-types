from abc import ABC
from dataclasses import dataclass
from typing import Any
from typing_extensions import Self

from ..utils import classproperty
from .common import Request, RequestHandler, register_preference


@dataclass(order=True, frozen=True)
class ImpersonateTarget:
    client: str | None = ...
    version: str | None = ...
    os: str | None = ...
    os_version: str | None = ...

    def __post_init__(self) -> None:
        ...

    def __contains__(self, target: Self) -> bool:
        ...

    @classmethod
    def from_str(cls, target: str) -> Self:
        ...


class ImpersonateRequestHandler(RequestHandler, ABC):
    _SUPPORTED_IMPERSONATE_TARGET_MAP: dict[ImpersonateTarget, Any] = ...

    def __init__(self, *, impersonate: ImpersonateTarget = ..., **kwargs: dict[str, Any]) -> None:
        ...

    @classproperty
    def supported_targets(self) -> tuple[ImpersonateTarget, ...]:
        ...

    def is_supported_target(self, target: ImpersonateTarget) -> bool:
        ...


@register_preference(ImpersonateRequestHandler)
def impersonate_preference(rh: RequestHandler, request: Request) -> int:
    ...
