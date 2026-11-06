from pydantic import BaseModel, Field, ConfigDict

class BebidaIngredienteCreate(BaseModel):
    id_bebida: int = Field(gt=0)
    id_ingrediente: int = Field(gt=0)
    cantidad: float = Field(gt=0)
    unidad: str = Field(min_length=1, max_length=20)

class BebidaIngredienteResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id_bebida: int
    id_ingrediente: int
    cantidad: float
    unidad: str

class BebidaIngredienteUpdate(BaseModel):
    id_bebida: int = Field(gt=0)
    id_ingrediente: int = Field(gt=0)
    cantidad: float = Field(gt=0)
    unidad: str = Field(min_length=1, max_length=20)

class BebidaIngredientePatch(BaseModel):
    cantidad: float | None = Field(default=None, gt=0)
    unidad: str | None = Field(default=None, min_length=1, max_length=20)