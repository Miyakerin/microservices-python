import asyncio
import base64
import logging
from contextlib import asynccontextmanager

import uvicorn
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.hazmat.primitives.asymmetric import rsa
from fastapi import FastAPI
import ssl

import src.recipes
from src.core.config import settings
from src.recipes.controllers.recipe_controller import db_help
from src.recipes.entities.base import Base
import py_eureka_client.eureka_client as eureka_client
from src.jwtUtil.jwt_util import JWTUtil

logger = logging.getLogger("uvicorn.error")

engine = db_help.engine


async def connect_to_eureka():
    eureka_url = f"http://{settings.eureka_settings.host}:{settings.eureka_settings.port}/eureka/"
    logger.info(f"Connecting to eureka at {eureka_url}")
    await eureka_client.init_async(
        eureka_server=eureka_url,
        app_name=settings.eureka_settings.app_name,
        instance_port=settings.fastapi_settings.port,
    )


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    await connect_to_eureka()
    asyncio.create_task(JWTUtil.load_keys(interval=1800))
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(src.recipes.controllers.recipe_controller.router)


if __name__ == "__main__":

    uvicorn.run(
        app, host=settings.fastapi_settings.host, port=settings.fastapi_settings.port
    )
