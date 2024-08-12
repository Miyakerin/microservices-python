from sqlalchemy import text
from fastapi import HTTPException

from src.dbUtil import db_helper
from src.core import config
from src.recipes.dto.recipe_dto import RecipeDto


db_settings = config.settings.recipes_db
engine = db_helper.DatabaseHelper(db_settings).engine


def get_recipes() -> list[RecipeDto]:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM recipe")).fetchall()
    return result


def get_recipe(recipe_id: int) -> RecipeDto:
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM recipe WHERE id = :id"), {"id": recipe_id}
        ).first()
    if result is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return result


def post_recipe(title: str, description: str) -> bool:
    with engine.connect() as conn:
        conn.execute(
            text(
                "INSERT INTO recipe (title, description) VALUES (:title, :description)"
            ),
            {"title": title, "description": description},
        )
        conn.commit()
    return True


def delete_recipe(recipe_id: int) -> bool:
    with engine.connect() as conn:
        conn.execute(text("DELETE FROM recipe WHERE id = :id"), {"id": recipe_id})
        conn.commit()
    return True
