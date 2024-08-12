from pydantic_settings import BaseSettings, SettingsConfigDict


class DbSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix='RECIPES_DB_', env_file='../../resources/.env', extra='ignore')
    user: str = 'user'
    password: str = 'password'
    db: str = 'db'
    host: str = 'localhost'
    port: int = 5432


class FastAPISettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix='FASTAPI_', env_file='../../resources/.env', extra='ignore')
    host: str = 'localhost'
    port: int = 8080


class Settings(BaseSettings):
    recipes_db: DbSettings = DbSettings()
    fastapi_settings: FastAPISettings = FastAPISettings()


settings = Settings()