from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from schemas.categoria import CategoriaCreate, CategoriaResponse, CategoriaUpdate
from app.dependencies import requiere_permiso
from services.categoria_service import (obtener_categoria,obtener_categorias,crear_categoria,editar_categoria, eliminar_categoria)

router = APIRouter(
    prefix="/api/categorias",
    tags=["Categorías"]
)

@router.get("/", response_model=list[CategoriaResponse])
def listar_categorias(
    db: Session = Depends(get_db),
):
    return obtener_categorias(db)

@router.get("/{id}", response_model=CategoriaResponse)
def consultar_categoria(
    id: int,
    db: Session = Depends(get_db),
):
    return obtener_categoria(id, db)

@router.post("/", response_model=CategoriaResponse)
def registrar_categoria(
    datos: CategoriaCreate,
    db: Session = Depends(get_db),
    usuario=Depends(requiere_permiso("categorias.crear"))
):
    return crear_categoria(datos, db)

@router.put("/{id}", response_model=CategoriaResponse)
def reemplazar_categoria(
    id: int,
    datos: CategoriaUpdate,
    db: Session = Depends(get_db),
    usuario=Depends(requiere_permiso("categorias.editar"))
):
    return editar_categoria(id, datos, db)

@router.delete("/{id}")
def borrar_categoria(id: int, db: Session = Depends(get_db), usuario=Depends(requiere_permiso("categorias.eliminar"))):
    return eliminar_categoria(id, db)