from typing import Sequence, Tuple, Any

from sqlalchemy import text, Row
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from src.recipes.entities.recipe_entity import Recipe


async def get_recipes(session: AsyncSession) -> Sequence[Row[tuple[Any, ...] | Any]]:
    result: Result = await session.execute(text("SELECT * FROM recipe"))
    return result.fetchall()


async def get_recipe(session: AsyncSession, recipe_id: int) -> Recipe | None:
    result: Result = await session.execute(
        text("SELECT * FROM recipe WHERE id = :id"), {"id": recipe_id}
    )
    return result.fetchone()


async def post_recipe(
    session: AsyncSession,
    title: str,
    description: str,
    calories: int,
    user_id: int = 0,
    spice_level: int = 0,
    is_deleted: bool = False,
) -> bool:
    await session.execute(
        text(
            "INSERT INTO recipe (title, description, user_id, calories, spice_level, is_deleted)"
            " VALUES (:title, :description, :user_id, :calories, :spice_level, :is_deleted)"
        ),
        {
            "title": title,
            "description": description,
            "user_id": user_id,
            "calories": calories,
            "spice_level": spice_level,
            "is_deleted": is_deleted,
        },
    )
    await session.commit()

    return True


async def delete_recipe(session: AsyncSession, recipe_id: int) -> bool:
    await session.execute(text("DELETE FROM recipe WHERE id = :id"), {"id": recipe_id})
    await session.commit()
    return True
