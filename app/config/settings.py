from os import environ
from typing import Any

from pydantic import BaseModel
from pydantic_settings import BaseSettings

class SessionData(BaseModel):
    scope: str
    user_id: str
    user_name: str


class Settings(BaseSettings):
    # DB
    db_user: str
    db_pass: str
    db_host: str
    db_port: int
    db_name: str

    default_message: str = "Your operation request can not be completed at the moment. " \
                           "Please try again later or contact our support department."


    class Config:
        env_file = ".env"


settings = Settings()