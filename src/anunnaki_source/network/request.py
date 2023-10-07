from dataclasses import dataclass
from aiohttp.typedefs import LooseCookies, StrOrURL, LooseHeaders
from aiohttp.helpers import BasicAuth, sentinel
from aiohttp.client_reqrep import Fingerprint
from ssl import SSLContext
from types import SimpleNamespace
from aiohttp.client import ClientTimeout
from typing import Any, Optional, Mapping, Iterable, Union

@dataclass
class Request:
    method: str
    url: StrOrURL
    params: Optional[Mapping[str, str]] = None
    data: Any = None
    json: Any = None
    cookies: Optional[LooseCookies] = None
    headers: Optional[LooseHeaders] = None
    skip_auto_headers: Optional[Iterable[str]] = None
    auth: Optional[BasicAuth] = None
    allow_redirects: bool = True
    max_redirects: int = 10
    compress: Optional[str] = None
    chunked: Optional[bool] = None
    expect100: bool = False
    raise_for_status: Optional[bool] = None
    read_until_eof: bool = True
    proxy: Optional[StrOrURL] = None
    proxy_auth: Optional[BasicAuth] = None
    timeout: Union[ClientTimeout, object] = sentinel
    verify_ssl: Optional[bool] = None
    fingerprint: Optional[bytes] = None
    ssl_context: Optional[SSLContext] = None
    ssl: Optional[Union[SSLContext, bool, Fingerprint]] = None
    proxy_headers: Optional[LooseHeaders] = None
    trace_request_ctx: Optional[SimpleNamespace] = None
    read_bufsize: Optional[int] = None