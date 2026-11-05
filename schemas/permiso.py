from pydantic import BaseModel, Field, ConfigDict
class PermisoCreate(BaseModel):
    nombre:str = Field (min_length=3,max_length=50)
class PermisoResponse(BaseModel):
    model_config= ConfigDict (from_attributes=True)
    id:int
    nombre:str
class PermisoUpdate(BaseModel):
    nombre:str | None= Field (default=None,min_length=3,max_length=50)
