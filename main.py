from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

import src.recipes
from src.core.config import settings
from src.recipes.services.recipe_services import engine
from src.recipes.entities.base import Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(src.recipes.controllers.recipe_controller.router)


if __name__ == "__main__":

    uvicorn.run(
        app, host=settings.fastapi_settings.host, port=settings.fastapi_settings.port
    )
