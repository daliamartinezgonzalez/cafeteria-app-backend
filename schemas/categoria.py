from pydantic import BaseModel, Field, ConfigDict

class CategoriaCreate(BaseModel):
    nombre_categoria: str = Field(min_length=3, max_length=20)

class CategoriaResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    nombre_categoria: str

class CategoriaUpdate(BaseModel):
    nombre_categoria: str = Field(min_length=3, max_length=20)