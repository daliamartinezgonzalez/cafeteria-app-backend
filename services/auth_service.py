from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.usuario import Usuario
from app.security import verify_password, crear_token_acceso

def iniciar_sesion(datos, db: Session):

    usuario = db.query(Usuario).filter(
        Usuario.email == datos.email
    ).first()

    if usuario is None:
        raise HTTPException(
            status_code=401,
            detail="Correo o contraseña incorrectos"
        )

    if not verify_password(datos.password, usuario.password):
        raise HTTPException(
            status_code=401,
            detail="Correo o contraseña incorrectos"
        )

    if not usuario.activo:
        raise HTTPException(
            status_code=403,
            detail="El usuario se encuentra inactivo"
        )

    token = crear_token_acceso({
        "sub": str(usuario.id)
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }