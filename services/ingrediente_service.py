from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from models.ingrediente import Ingrediente
from models.bebida import Bebida
from models.bebida_ingrediente import BebidaIngrediente

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
    nombre = datos.nombre.strip()
    ingrediente_existente = db.query(Ingrediente).filter(
        func.lower(Ingrediente.nombre) == nombre.lower()
    ).first()
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
        nombre = datos.nombre.strip()
        ingrediente_existente = db.query(Ingrediente).filter(
            func.lower(Ingrediente.nombre) == nombre.lower()
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
    # se verifica si el ingrediente esta relacionado con alguna bebida
    ingrediente_asociado = db.query(BebidaIngrediente).filter(
        BebidaIngrediente.id_ingrediente == id
    ).first()
    if ingrediente_asociado:
        raise HTTPException(
            status_code=409,
            detail="No se puede eliminar el ingrediente porque esta relacionado con una o mas bebidas"
        )
    db.delete(ingrediente)
    db.commit()
    return {"mensaje": "Ingrediente eliminado correctamente"}