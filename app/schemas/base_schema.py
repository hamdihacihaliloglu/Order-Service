from typing import Optional

from pydantic import BaseModel


class ResponseWithMessage(BaseModel):
    status: bool
    message: str