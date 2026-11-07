from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.dependencies import requiere_permiso
from schemas.bebida import BebidaCreate, BebidaResponse, BebidaUpdate, BebidaPatch

from services.bebida_service import (
    obtener_bebida,
    obtener_bebidas,
    crear_bebida,
    editar_bebida,
    actualizar_bebida,
    eliminar_bebida
)

router = APIRouter(
    prefix="/api/bebidas",
    tags=["Bebidas"]
)


@router.get("/", response_model=list[BebidaResponse])
def listar_bebidas(
    db: Session = Depends(get_db),
):
    return obtener_bebidas(db)

@router.get("/{id}", response_model=BebidaResponse)
def consultar_bebida(
    id: int,
    db: Session = Depends(get_db),
):
    return obtener_bebida(id, db)

@router.post("/", response_model=BebidaResponse)
def registrar_bebida(
    datos: BebidaCreate,
    db: Session = Depends(get_db),
    usuario=Depends(requiere_permiso("bebidas.crear"))
):
    return crear_bebida(datos, db)

@router.put("/{id}", response_model=BebidaResponse)
def reemplazar_bebida(
    id: int,
    datos: BebidaUpdate,
    db: Session = Depends(get_db),
    usuario=Depends(requiere_permiso("bebidas.editar"))
):
    return editar_bebida(id, datos, db)

@router.patch("/{id}", response_model=BebidaResponse)
def actualizar_bebida_parcial(
    id: int,
    datos: BebidaPatch,
    db: Session = Depends(get_db),
    usuario=Depends(requiere_permiso("bebidas.editar"))
):
    return actualizar_bebida(id, datos, db)

@router.delete("/{id}")
def borrar_bebida(
    id: int,
    db: Session = Depends(get_db),
    usuario=Depends(requiere_permiso("bebidas.eliminar"))
):
    return eliminar_bebida(id, db)