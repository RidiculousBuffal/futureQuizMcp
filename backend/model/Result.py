from typing import Any

from pydantic import BaseModel


class Result(BaseModel):
    code: int
    msg: str
    data: Any
