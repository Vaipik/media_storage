import json
from functools import lru_cache
from pathlib import Path

from pydantic import BaseSettings, validator


class DB(BaseSettings):
    host: str
    port: int
    name: str
    user: str
    password: str


class GDrive(BaseSettings):
    folder: str
    credentials: dict
    scopes: list[str]

    @validator('credentials', pre=True)
    def json_decode_credentials(cls, v):
        if isinstance(v, str):
            try:
                return json.loads(v)
            except ValueError:
                pass
        return v

    @validator('scopes', pre=True)
    def json_decode_scopes(cls, v):
        if isinstance(v, str):
            try:
                return json.loads(v)
            except ValueError:
                pass
        return v


class Settings(BaseSettings):
    db: DB
    gdrive: GDrive

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        env_nested_delimiter = "__"


@lru_cache
def load_config(env_file=".env") -> Settings:
    BASE_DIR = Path(__file__).parent.parent
    settings = Settings(_env_file=BASE_DIR / env_file)
    return settings
