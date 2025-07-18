import abc

from .common import RequestHandler, Response


class WebSocketResponse(Response):
    def send(self, message: bytes | str) -> object:
        ...

    def recv(self) -> object:
        ...


class WebSocketRequestHandler(RequestHandler, abc.ABC):
    ...
