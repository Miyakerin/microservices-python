from pydantic import BaseModel, ConfigDict


class RecipeDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str
    description: str
