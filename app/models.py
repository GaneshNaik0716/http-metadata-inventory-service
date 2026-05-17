from pydantic import BaseModel, HttpUrl
from typing import Dict, Any


class URLRequest(BaseModel):
    url: HttpUrl


class MetadataResponse(BaseModel):
    url: str
    headers: Dict[str, Any]
    cookies: Dict[str, Any]
    page_source: str