import os
from pathlib import Path
from typing import ClassVar

from pydantic import BaseModel, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8080


class DatabaseConfig(BaseModel):
    url: str
    user: str
    password: str
    pgadmin_email: str
    pgadmin_password: str
    echo: bool = False
    echo_pool: bool = False
    max_overflow: int = 10
    pool_size: int = 5


class Settings(BaseSettings):
    db: DatabaseConfig
    model_config = SettingsConfigDict(
        env_file=(".env.template", ".env"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__",
    )
    run: RunConfig = RunConfig()
    db: DatabaseConfig


settings = Settings()
