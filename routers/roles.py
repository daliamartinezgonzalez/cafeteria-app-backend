from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from schemas.rol import RolResponse
from app.dependencies import requiere_permiso

from services.rol_service import (
    obtener_roles,
    obtener_rol,
)

router = APIRouter(
    prefix="/api/roles",
    tags=["Roles"]
)

# para ver todos los roles
@router.get("/", response_model=list[RolResponse])
def listar_roles(db: Session = Depends(get_db), usuario=Depends(requiere_permiso("roles.ver"))):
    return obtener_roles(db)

#para ver los datos de un rol especifico
@router.get("/{id}", response_model=RolResponse)
def consultar_roles(id: int, db: Session = Depends(get_db), usuario=Depends(requiere_permiso("roles.ver"))):
    return obtener_rol(id, db)
