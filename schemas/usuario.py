from pydantic import EmailStr, BaseModel, Field, ConfigDict
class UsuarioCreate(BaseModel):
    nombre: str
    apellido_p: str
    apellido_m: str | None = None
    email: EmailStr
    password: str = Field(min_length=8, max_length=64)
    id_rol: int
class UsuarioResponse(BaseModel):
    model_config= ConfigDict (from_attributes=True)
    id: int
    nombre: str
    apellido_p: str
    apellido_m: str | None = None
    email: EmailStr
    activo: bool
    id_rol: int
    
class UsuarioUpdate(BaseModel):
    nombre: str | None = Field(default=None, min_length=2, max_length=50)
    apellido_p: str | None =None
    apellido_m: str | None = None
    email: EmailStr | None =None
    id_rol: int

class UsuarioReplace(BaseModel):
    nombre: str
    apellido_p: str
    apellido_m: str | None = None
    email: EmailStr
    activo: bool
    id_rol: int