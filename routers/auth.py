from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies import obtener_usuario_actual

from services.auth_service import iniciar_sesion

from models.usuario import Usuario
from schemas.auth import LoginRequest, TokenResponse
from schemas.usuario import UsuarioResponse


router = APIRouter(prefix="/api/auth", tags=["Autenticación"])


@router.post("/login", response_model=TokenResponse)
def login(datos: LoginRequest, db: Session = Depends(get_db)):
    return iniciar_sesion(datos, db)


@router.get("/me", response_model=UsuarioResponse)
def consultar_usuario_actual(
    usuario: Usuario = Depends(obtener_usuario_actual)
):
    return usuario