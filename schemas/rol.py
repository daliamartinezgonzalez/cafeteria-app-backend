from pydantic import BaseModel, Field, ConfigDict

class RolCreate (BaseModel):
    nombre: str = Field(min_length=3, max_length=50)
    
class RolResponse(BaseModel):
    model_config= ConfigDict (from_attributes=True)
    id:int
    nombre: str

class RolUpdate(BaseModel):
    nombre: str | None = Field(default=None, min_length=3, max_length=50)