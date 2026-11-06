from pydantic import EmailStr, BaseModel, Field, ConfigDict

class RolResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    nombre: str
    
class UsuarioCreate(BaseModel):
    nombre: str = Field(min_length=2, max_length=50)
    apellido_p: str = Field(min_length=2, max_length=50)
    apellido_m: str | None = Field(default=None, max_length=50)
    email: EmailStr
    password: str = Field(min_length=8, max_length=64)
    id_rol: int = Field(gt=0)
class UsuarioResponse(BaseModel):
    model_config= ConfigDict (from_attributes=True)
    id: int
    nombre: str
    apellido_p: str
    apellido_m: str | None = None
    email: EmailStr
    activo: bool
    id_rol: int
    rol: RolResponse
    
class UsuarioUpdate(BaseModel):
    nombre: str | None = Field(default=None, min_length=2, max_length=50)
    apellido_p: str | None = Field(default=None, min_length=2, max_length=50)
    apellido_m: str | None = Field(default=None, max_length=50)
    email: EmailStr | None =None
    activo: bool | None =None
    id_rol: int | None = Field(default=None, gt=0)

class UsuarioReplace(BaseModel):
    nombre: str = Field(min_length=2, max_length=50)
    apellido_p: str = Field(min_length=2, max_length=50)
    apellido_m: str | None = Field(default=None, max_length=50)
    email: EmailStr
    activo: bool 
    id_rol: int = Field(gt=0)