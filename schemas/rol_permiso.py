from pydantic import BaseModel, Field, ConfigDict
class RolPermisoCreate(BaseModel):
    id_permiso:int = Field (gt=0)
    id_rol:int = Field (gt=0)
class RolPermisoResponse(BaseModel):
    model_config= ConfigDict (from_attributes=True)
    
    id_permiso:int
    id_rol:int
