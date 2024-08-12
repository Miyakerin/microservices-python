from fastapi import APIRouter
from src.recipes.services import recipe_services
from src.recipes.dto.recipe_dto import RecipeDto

router = APIRouter(prefix="/api/recipes", tags=["Recipes"])


@router.get("/")
def get_recipes() -> list[RecipeDto]:
    return recipe_services.get_recipes()


@router.get("/{recipe_id}/")
def get_recipe(recipe_id: int) -> RecipeDto:
    return recipe_services.get_recipe(recipe_id)


@router.post("/")
def create_recipe(title: str, description: str) -> bool:
    return recipe_services.post_recipe(title, description)


@router.delete("/{recipe_id}/")
def delete_recipe(recipe_id: int) -> bool:
    return recipe_services.delete_recipe(recipe_id)
