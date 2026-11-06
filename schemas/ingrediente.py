from pydantic import BaseModel, Field, ConfigDict

class IngredienteCreate(BaseModel):
    nombre: str = Field(min_length=3, max_length=20)

class IngredienteResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    nombre: str

class IngredienteUpdate(BaseModel):
    nombre: str = Field(min_length=3, max_length=20)