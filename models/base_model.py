from typing import Optional

from pydantic import BaseModel, Field, HttpUrl


class RepositoryResponse(BaseModel):
    id: int
    name: str
    full_name: str
    private: bool
    description: Optional[str] = None
    html_url: HttpUrl


class RateLimitResponse(BaseModel):
    limit: int = Field(alias="x-ratelimit-limit")
    remaining: int = Field(alias="x-ratelimit-remaining")
    used: int = Field(alias="x-ratelimit-used")
    reset: int = Field(alias="x-ratelimit-reset")
    resource: str = Field(alias="x-ratelimit-resource")
