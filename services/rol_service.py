from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.rol import Rol

# llamada a la base de datos para mostrar todos los roles
def obtener_roles(db: Session):
    return db.query(Rol).all()

# llamada a la base de datos para filtrar a solo un rol y mostrar ese
def obtener_rol(id: int, db: Session):
    rol = db.query(Rol).filter(Rol.id == id).first()

    if rol is None:
        raise HTTPException(
            status_code=404,
            detail="rol no encontrado"
        )

    return rol
