import os
from typing import Literal

from pydantic import computed_field, PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

ENVIRONMENT = os.getenv("ENVIRONMENT", "local")
env_file = None
if ENVIRONMENT in {"local", "staging", "production"}:
    env_file = os.path.normpath(os.path.join(os.path.dirname(__file__), f"../../.env.{ENVIRONMENT}"))
else:
    raise ValueError("环境变量 ENVIRONMENT 的值只能是 local, staging, 或 production")

exists_env_file = "存在" if os.path.exists(env_file) else "缺失"
print(f"当前使用的配置文件（{exists_env_file}）={env_file}")


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=env_file, env_ignore_empty=True, extra="ignore")

    ENVIRONMENT: Literal["local", "staging", "production"] = "local"
    PROJECT_NAME: str = "FastAPI Template"
    APP_URL: str = "http://127.0.0.1:8000"
    API_STR: str = "/api/v1"

    STATIC_DIR: str = os.path.normpath(os.path.join(os.path.dirname(__file__), f"./../../static"))

    POSTGRES_SERVER: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "example_db"

    @computed_field
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> PostgresDsn:
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_SERVER,
            port=self.POSTGRES_PORT,
            path=self.POSTGRES_DB,
        )


settings = Settings()
print(f'环境变量加载完成，APP_URL={settings.APP_URL or "settings.APP_URL 未配置"}')
