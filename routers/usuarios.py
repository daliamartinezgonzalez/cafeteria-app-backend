from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from schemas.usuario import UsuarioResponse, UsuarioCreate, UsuarioUpdate, UsuarioReplace
from app.dependencies import requiere_permiso

from services.usuario_service import (
    obtener_usuarios,
    obtener_usuario,
    crear_usuario,
    editar_usuario,
    actualizar_usuario,
    eliminar_usuario
)

router = APIRouter(
    prefix="/api/usuarios",
    tags=["Usuarios"]
)

# para ver todos los usuarios
@router.get("/", response_model=list[UsuarioResponse])
def listar_usuarios(db: Session = Depends(get_db), usuario=Depends(requiere_permiso("usuarios.ver"))):
    return obtener_usuarios(db)

#para ver los datos de un usuario especifico
@router.get("/{id}", response_model=UsuarioResponse)
def consultar_usuario(id: int, db: Session = Depends(get_db), usuario=Depends(requiere_permiso("usuarios.ver"))):
    return obtener_usuario(id, db)

#para crear un usuario
@router.post("/", response_model=UsuarioResponse)
def registrar_usuario(datos: UsuarioCreate, db: Session = Depends(get_db), usuario=Depends(requiere_permiso("usuarios.crear"))):
    return crear_usuario(datos, db)

#para editar un usuario
@router.put("/{id}", response_model=UsuarioResponse)
def reemplazar_usuario(
    id: int,
    datos: UsuarioReplace,
    db: Session = Depends(get_db),
    usuario=Depends(requiere_permiso("usuarios.editar"))
):
    return editar_usuario(id, datos, db)

# para editar un usuario parcialmente
@router.patch("/{id}", response_model=UsuarioResponse)
def modificar_usuario(
    id: int,
    datos: UsuarioUpdate,
    db: Session = Depends(get_db),
    usuario=Depends(requiere_permiso("eliminar.editar"))
):
    return actualizar_usuario(id, datos, db)

# eliminar un usuario
@router.delete("/{id}")
def borrar_usuario(id: int, db: Session = Depends(get_db), usuario=Depends(requiere_permiso("usuarios.eliminar"))):
    return eliminar_usuario(id, db)