import uvicorn
from fastapi import FastAPI

from recipes.controllers import RecipeController

from core.config import Settings

app = FastAPI()
app.include_router(RecipeController.router)

if __name__ == '__main__':
    settings = Settings()
    uvicorn.run(app, host=settings.fastapi_settings.host, port=settings.fastapi_settings.port)
