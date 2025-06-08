import urllib
import urllib.request
import xml.etree.ElementTree as ET

from yt_dlp.networking import Request


class compat_HTMLParseError(ValueError):
    ...


def compat_etree_fromstring(text: str) -> ET.Element[str]:
    ...


def compat_ord(c: str) -> int:
    ...


def compat_expanduser(path: str) -> str:
    ...


def urllib_req_to_req(urllib_request: urllib.request.Request) -> Request:
    ...
