from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.core import config
from src.recipes.entities.recipe_entity import Recipe
from src.recipes.services import recipe_services
from typing import Sequence
from src.dbUtil.db_helper import DatabaseHelper

router = APIRouter(prefix="/api/recipes", tags=["Recipes"])
db_settings = config.settings.recipes_db
db_help = DatabaseHelper(db_settings)


@router.get("")
async def get_recipes(
    session: AsyncSession = Depends(db_help.session_dependency),
) -> Sequence[Recipe]:
    return await recipe_services.get_recipes(session)


@router.get("/{recipe_id}")
async def get_recipe(
    recipe_id: int, session: AsyncSession = Depends(db_help.session_dependency)
) -> Recipe:
    product = await recipe_services.get_recipe(session, recipe_id)
    if product is not None:
        return product
    raise HTTPException(status_code=404, detail="Recipe not found")


@router.post("")
async def create_recipe(
    title: str,
    description: str,
    session: AsyncSession = Depends(db_help.session_dependency),
) -> bool:
    return await recipe_services.post_recipe(session, title, description)


@router.delete("/{recipe_id}")
async def delete_recipe(
    recipe_id: int, session: AsyncSession = Depends(db_help.session_dependency)
) -> bool:
    return await recipe_services.delete_recipe(session, recipe_id)
