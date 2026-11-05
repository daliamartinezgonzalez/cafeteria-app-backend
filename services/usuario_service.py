from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.usuario import Usuario
from models.rol import Rol
from app.security import hash_password

# llamada a la base de datos para mostrar todos los usuarios
def obtener_usuarios(db: Session):
    return db.query(Usuario).all()

# llamada a la base de datos para filtrar a solo un usuario y mostrar ese
def obtener_usuario(id: int, db: Session):
    usuario = db.query(Usuario).filter(Usuario.id == id).first()

    if usuario is None:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    return usuario

# para crear un usuario y devolver errores de ser necesario
def crear_usuario(datos, db: Session):
    usuario_existente = db.query(Usuario).filter(
        Usuario.email == datos.email
    ).first()

    if usuario_existente:
        raise HTTPException(
            status_code=409,
            detail="Este correo electrónico ya está registrado"
        )

    rol = db.query(Rol).filter(Rol.id == datos.id_rol).first()

    if rol is None:
        raise HTTPException(
            status_code=404,
            detail="El rol seleccionado no existe"
        )

    datos_usuario = datos.model_dump()
    datos_usuario["password"] = hash_password(datos_usuario["password"])

    usuario = Usuario(**datos_usuario)

    db.add(usuario)
    db.commit()
    db.refresh(usuario)

    return usuario

# para editar usuario
def editar_usuario(id: int, datos, db: Session):
    usuario = obtener_usuario(id, db)

    if datos.email != usuario.email:
        usuario_existente = db.query(Usuario).filter(
            Usuario.email == datos.email
        ).first()

        if usuario_existente:
            raise HTTPException(
                status_code=409,
                detail="Este correo electrónico ya está registrado"
            )

    rol = db.query(Rol).filter(Rol.id == datos.id_rol).first()

    if rol is None:
        raise HTTPException(
            status_code=404,
            detail="El rol seleccionado no existe"
        )

    datos_actualizados = datos.model_dump()

    for campo, valor in datos_actualizados.items():
        setattr(usuario, campo, valor)

    db.commit()
    db.refresh(usuario)

    return usuario

# para editar usuario completamente
def actualizar_usuario(id: int, datos, db: Session):
    usuario = obtener_usuario(id, db)

    datos_actualizados = datos.model_dump(exclude_unset=True)

    if "email" in datos_actualizados:
        usuario_existente = db.query(Usuario).filter(
            Usuario.email == datos_actualizados["email"],
            Usuario.id != id
        ).first()

        if usuario_existente:
            raise HTTPException(
                status_code=409,
                detail="Este correo electrónico ya está registrado"
            )

    if "id_rol" in datos_actualizados:
        rol = db.query(Rol).filter(
            Rol.id == datos_actualizados["id_rol"]
        ).first()

        if rol is None:
            raise HTTPException(
                status_code=404,
                detail="El rol seleccionado no existe"
            )

    for campo, valor in datos_actualizados.items():
        setattr(usuario, campo, valor)

    db.commit()
    db.refresh(usuario)

    return usuario


def eliminar_usuario(id: int, db: Session):
    usuario = obtener_usuario(id, db)

    db.delete(usuario)
    db.commit()

    return {"mensaje": "Usuario eliminado correctamente"}