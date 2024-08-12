import uvicorn
from fastapi import FastAPI

import src.recipes
from src.core.config import settings


app = FastAPI()
app.include_router(src.recipes.controllers.recipe_controller.router)


if __name__ == "__main__":

    uvicorn.run(
        app, host=settings.fastapi_settings.host, port=settings.fastapi_settings.port
    )
