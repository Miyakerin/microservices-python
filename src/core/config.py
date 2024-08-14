from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class RecipesDbSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="RECIPES_DB_", extra="ignore")
    user: str = "user"
    password: str = "password"
    db: str = "db"
    host: str = "localhostdfdf"
    port_host: int = 5432
    echo: bool = True


class FastAPISettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="FASTAPI_", extra="ignore")
    host: str = "localhost"
    port: int = 8080


class EurekaSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="EUREKA_", extra="ignore")
    host: str = "localhost"
    port: int = 8081
    app_name: str = "app_name"


class AuthSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="AUTHSERVICE_", extra="ignore")
    domain_name: str = "domain_name"
    public_key: str = "public_key"


class Settings(BaseSettings):
    recipes_db: RecipesDbSettings = RecipesDbSettings()
    fastapi_settings: FastAPISettings = FastAPISettings()
    eureka_settings: EurekaSettings = EurekaSettings()
    auth_settings: AuthSettings = AuthSettings()


settings = Settings()
