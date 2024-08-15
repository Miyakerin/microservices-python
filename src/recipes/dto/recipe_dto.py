from pydantic import BaseModel, ConfigDict


class RecipeDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    title: str
    description: str
    user_id: int
    calories: int
    spice_level: int
    is_deleted: bool
