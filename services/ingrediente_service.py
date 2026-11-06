from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.ingrediente import Ingrediente

def obtener_ingredientes(db: Session):
    return db.query(Ingrediente).all()

def obtener_ingrediente(id: int, db: Session):
    ingrediente = db.query(Ingrediente).filter(Ingrediente.id == id).first()
    # si no existe el ingrediente que se esta buscando
    if ingrediente is None:
        raise HTTPException(
            status_code=404,
            detail="Ingrediente no encontrado"
        )

    return ingrediente

def crear_ingrediente(datos,db:Session):
    ingrediente_existente = db.query(Ingrediente).filter(Ingrediente.nombre== datos.nombre).first()
    # como el nombre es unico se muestra el error en caso de que se quiera registrar uno igual
    if ingrediente_existente: 
        raise HTTPException(
            status_code=409,
            detail="Ingrediente Existente"
        )
    datos_ingrediente= datos.model_dump()
    ingrediente=Ingrediente(**datos_ingrediente)
    db.add(ingrediente)
    db.commit()
    db.refresh(ingrediente)
    return ingrediente

def editar_ingrediente(id: int, datos, db: Session):
    ingrediente = obtener_ingrediente(id, db)

    if datos.nombre != ingrediente.nombre:
        ingrediente_existente = db.query(Ingrediente).filter(
            Ingrediente.nombre == datos.nombre
        ).first()

        if ingrediente_existente:
            raise HTTPException(
                status_code=409,
                detail="Ingrediente ya registrado"
            )

    ingrediente.nombre = datos.nombre

    db.commit()
    db.refresh(ingrediente)

    return ingrediente

def eliminar_ingrediente(id: int, db: Session):
    ingrediente = obtener_ingrediente(id, db)

    db.delete(ingrediente)
    db.commit()

    return {"mensaje": "Ingrediente eliminado correctamente"}