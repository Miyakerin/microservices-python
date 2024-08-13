from typing import Any, Sequence

from sqlalchemy import text, Row, RowMapping
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result

from src.dbUtil import db_helper
from src.core import config
from src.recipes.entities.recipe_entity import Recipe


async def get_recipes(session: AsyncSession) -> Sequence[Recipe]:
    result: Result = await session.execute(text("SELECT * FROM recipe"))
    return result.scalars().all()


async def get_recipe(session: AsyncSession, recipe_id: int) -> Recipe | None:
    result: Result = await session.execute(
        text("SELECT * FROM recipe WHERE id = :id"), {"id": recipe_id}
    )
    return result.scalars().first()


async def post_recipe(session: AsyncSession, title: str, description: str) -> bool:
    await session.execute(
        text("INSERT INTO recipe (title, description) VALUES (:title, :description)"),
        {"title": title, "description": description},
    )
    await session.commit()

    return True


async def delete_recipe(session: AsyncSession, recipe_id: int) -> bool:
    await session.execute(text("DELETE FROM recipe WHERE id = :id"), {"id": recipe_id})
    await session.commit()
    return True
