from pydantic import BaseModel


class RecipeDto(BaseModel):
    id: int
    title: str
    description: str
