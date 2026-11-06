from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from schemas.ingrediente import IngredienteCreate,IngredienteResponse,IngredienteUpdate
from app.dependencies import requiere_permiso
from services.ingrediente_service import (obtener_ingrediente,obtener_ingredientes,crear_ingrediente,editar_ingrediente, eliminar_ingrediente)

router = APIRouter(
    prefix="/api/ingredientes",
    tags=["Ingredientes"]
)

@router.get("/", response_model=list[IngredienteResponse])
def listar_ingredientes(
    db: Session = Depends(get_db),
    usuario=Depends(requiere_permiso("ingredientes.ver"))
):
    return obtener_ingredientes(db)

@router.get("/{id}", response_model=IngredienteResponse)
def consultar_ingrediente(
    id: int,
    db: Session = Depends(get_db),
    usuario=Depends(requiere_permiso("ingredientes.ver"))
):
    return obtener_ingrediente(id, db)

@router.post("/", response_model=IngredienteResponse)
def registrar_ingrediente(
    datos: IngredienteCreate,
    db: Session = Depends(get_db),
    usuario=Depends(requiere_permiso("ingredientes.crear"))
):
    return crear_ingrediente(datos, db)

@router.put("/{id}", response_model=IngredienteResponse)
def reemplazar_ingrediente(
    id: int,
    datos: IngredienteUpdate,
    db: Session = Depends(get_db),
    usuario=Depends(requiere_permiso("ingredientes.editar"))
):
    return editar_ingrediente(id, datos, db)

@router.delete("/{id}")
def borrar_ingrediente(id: int, db: Session = Depends(get_db), usuario=Depends(requiere_permiso("ingredientes.eliminar"))):
    return eliminar_ingrediente(id, db)