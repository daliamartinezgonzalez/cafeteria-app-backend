from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from app.database import get_db
from app.security import verificar_token
from models.usuario import Usuario

bearer_scheme = HTTPBearer()

def obtener_usuario_actual(
    credenciales: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    db: Session = Depends(get_db)
):
    token = credenciales.credentials
    datos_token = verificar_token(token)

    if datos_token is None:
        raise HTTPException(
            status_code=401,
            detail="Token inválido o expirado"
        )

    id_usuario = datos_token.get("sub")

    if id_usuario is None:
        raise HTTPException(
            status_code=401,
            detail="Token inválido"
        )

    usuario = db.query(Usuario).filter(
        Usuario.id == int(id_usuario)
    ).first()

    if usuario is None or not usuario.activo:
        raise HTTPException(
            status_code=401,
            detail="Usuario no autorizado"
        )

    return usuario