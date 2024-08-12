from fastapi import APIRouter

router = APIRouter(prefix="/api/recipes")

@router.get("/")
def get_recipes():
    pass

@router.get("/{recipe_id}/")
def get_recipe(recipe_id):
    pass

@router.post("/")
def create_recipe(recipe):
    pass

@router.delete("/{recipe_id}/")
def delete_recipe(recipe_id):
    pass