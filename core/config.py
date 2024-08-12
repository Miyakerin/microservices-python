import os

from poetry.console.commands import self
from pydantic import Field, BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class DbSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix='RECIPES_DB_', env_file='../.env', extra='ignore')
    user: str = 'user'
    password: str = 'password'
    db: str = 'db'
    host: str = 'localhost'
    port: int = 5432


class Settings(BaseSettings):
    recipes_db: DbSettings = DbSettings()


settings = Settings()

print(settings)
