from abc import ABC
from dataclasses import dataclass
from typing_extensions import Self

from .common import Request, RequestHandler


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
    _SUPPORTED_IMPERSONATE_TARGET_MAP: dict[ImpersonateTarget, object] = ...

    def __init__(self, *, impersonate: ImpersonateTarget | None = None, **kwargs: object) -> None:
        ...

    @property
    def supported_targets(cls) -> tuple[ImpersonateTarget, ...]:
        ...

    def is_supported_target(self, target: ImpersonateTarget) -> bool:
        ...


def impersonate_preference(rh: RequestHandler, request: Request) -> int:
    ...
