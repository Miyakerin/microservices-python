from typing import Sequence, Tuple, Any

from fastapi import Header, HTTPException
from sqlalchemy import text, Row
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from src.recipes.entities.recipe_entity import Recipe

from src.jwtUtil.jwt_util import JWTUtil


async def get_recipes(
    session: AsyncSession, Authorization: str
) -> Sequence[Row[tuple[Any, ...] | Any]]:
    claims = JWTUtil.get_claims(Authorization)
    if claims.get("role", "USER") == "ADMIN":
        result: Result = await session.execute(text("SELECT * FROM recipe"))
        return result.fetchall()
    raise HTTPException(status_code=403, detail="Forbidden")


async def get_recipe(
    session: AsyncSession, Authorization: str, recipe_id: int
) -> Recipe | None:
    claims = JWTUtil.get_claims(Authorization)
    result = (
        await session.execute(
            text("SELECT * FROM recipe WHERE id = :id"), {"id": recipe_id}
        )
    ).fetchone()
    if result.__dict__.get("user_id") == claims["sub"] or claims["role"] == "ADMIN":
        return result.fetchone()
    raise HTTPException(status_code=403, detail="Forbidden")


async def post_recipe(
    session: AsyncSession,
    Authorization: str,
    title: str,
    description: str,
    calories: int,
    user_id: int = 0,
    spice_level: int = 0,
    is_deleted: bool = False,
) -> bool:
    claims = JWTUtil.get_claims(Authorization)
    if claims.get("role", "USER") != "ADMIN":
        raise HTTPException(status_code=403, detail="Forbidden")
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


async def delete_recipe(
    session: AsyncSession, Authorization: str, recipe_id: int
) -> bool:
    claims = JWTUtil.get_claims(Authorization)
    recipe = await get_recipe(session, Authorization, recipe_id)
    if claims.get("role", "USER") == "ADMIN" or claims["iss"] == recipe.user_id:
        await session.execute(
            text("DELETE FROM recipe WHERE id = :id"), {"id": recipe_id}
        )
        await session.commit()
        return True
    raise HTTPException(status_code=403, detail="Forbidden")
