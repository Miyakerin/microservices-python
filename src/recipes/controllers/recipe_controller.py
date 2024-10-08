from typing import Sequence, Any

from fastapi import APIRouter, HTTPException, Depends, Header
from sqlalchemy import Row
from sqlalchemy.ext.asyncio import AsyncSession
import logging

from src.core import config
from src.dbUtil.db_helper import DatabaseHelper
from src.recipes.dto.recipe_dto import RecipeDTO
from src.recipes.entities.recipe_entity import Recipe
from src.recipes.services import recipe_services

router = APIRouter(prefix="/api/recipes", tags=["Recipes"])
db_settings = config.settings.recipes_db
db_help = DatabaseHelper(db_settings)
logger = logging.getLogger("uvicorn.error")


@router.get("", response_model=list[RecipeDTO])
async def get_recipes(
    Authorization: str = Header(None),
    session: AsyncSession = Depends(db_help.scoped_session_dependency),
) -> Sequence[Row[tuple[Any, ...] | Any]]:
    return await recipe_services.get_recipes(session, Authorization)


@router.get("/{recipe_id}", response_model=RecipeDTO)
async def get_recipe(
    recipe_id: int,
    Authorization: str = Header(None),
    session: AsyncSession = Depends(db_help.scoped_session_dependency),
) -> Recipe:
    product = await recipe_services.get_recipe(session, Authorization, recipe_id)
    if product is not None:
        return product
    raise HTTPException(status_code=404, detail="Recipe not found")


@router.post("")
async def create_recipe(
    title: str,
    description: str,
    calories: int,
    spice_level: int,
    Authorization: str = Header(None),
    session: AsyncSession = Depends(db_help.scoped_session_dependency),
) -> bool:
    return await recipe_services.post_recipe(
        session, Authorization, title, description, calories, spice_level=spice_level
    )


@router.delete("/{recipe_id}")
async def delete_recipe(
    recipe_id: int,
    Authorization: str = Header(None),
    session: AsyncSession = Depends(db_help.scoped_session_dependency),
) -> bool:
    return await recipe_services.delete_recipe(session, Authorization, recipe_id)
