from pydantic import BaseModel, Field, ConfigDict

class BebidaIngredienteCreate(BaseModel):
    id_ingrediente: int = Field(gt=0)
    cantidad: float = Field(gt=0)
    unidad: str = Field(min_length=1, max_length=20)

class BebidaIngredienteResponse(BaseModel):
    id_ingrediente: int
    nombre: str
    cantidad: float
    unidad: str

class BebidaCreate(BaseModel):
    nombre: str = Field(min_length=3, max_length=100)
    descripcion: str | None = Field(default=None, max_length=255)
    precio: float = Field(gt=0)
    tamaño: str = Field(min_length=1, max_length=30)
    imagen_url: str = Field(min_length=1, max_length=255)
    id_categoria: int = Field(gt=0)
    ingredientes: list[BebidaIngredienteCreate] = Field(min_length=1)

class BebidaResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    nombre: str
    descripcion: str | None
    precio: float
    tamaño: str
    imagen_url: str
    id_categoria: int
    ingredientes: list[BebidaIngredienteResponse]

class BebidaUpdate(BaseModel):
    nombre: str = Field(min_length=3, max_length=100)
    descripcion: str | None = Field(default=None, max_length=255)
    precio: float = Field(gt=0)
    tamaño: str = Field(min_length=1, max_length=30)
    imagen_url: str = Field(min_length=1, max_length=255)
    id_categoria: int = Field(gt=0)
    ingredientes: list[BebidaIngredienteCreate] = Field(min_length=1)

class BebidaPatch(BaseModel):
    nombre: str | None = Field(default=None, min_length=3, max_length=100)
    descripcion: str | None = Field(default=None, max_length=255)
    precio: float | None = Field(default=None, gt=0)
    tamaño: str | None = Field(default=None, min_length=1, max_length=30)
    imagen_url: str | None = Field(default=None, min_length=1, max_length=255)
    id_categoria: int | None = Field(default=None, gt=0)
    ingredientes: list[BebidaIngredienteCreate] | None = Field(
        default=None,
        min_length=1
    )