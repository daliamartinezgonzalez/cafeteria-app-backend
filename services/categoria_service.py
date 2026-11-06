from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.categoria import Categoria

def obtener_categorias(db: Session):
    return db.query(Categoria).all()

def obtener_categoria(id: int, db: Session):
    categoria = db.query(Categoria).filter(Categoria.id == id).first()
    # si no existe la categoria que se esta buscando
    if categoria is None:
        raise HTTPException(
            status_code=404,
            detail="Categoría no encontrada"
        )

    return categoria

def crear_categoria(datos,db:Session):
    categoria_existente = db.query(Categoria).filter(Categoria.nombre_categoria== datos.nombre_categoria).first()
    # como el nombre es unico se muestra el error en caso de que se quiera registrar uno igual
    if categoria_existente: 
        raise HTTPException(
            status_code=409,
            detail="Categoria Existente"
        )
    datos_categoria= datos.model_dump()
    categoria=Categoria(**datos_categoria)
    db.add(categoria)
    db.commit()
    db.refresh(categoria)
    return categoria

def editar_categoria(id: int, datos, db: Session):
    categoria = obtener_categoria(id, db)

    if datos.nombre_categoria != categoria.nombre_categoria:
        categoria_existente = db.query(Categoria).filter(
            Categoria.nombre_categoria == datos.nombre_categoria
        ).first()

        if categoria_existente:
            raise HTTPException(
                status_code=409,
                detail="Categoría ya registrada"
            )

    categoria.nombre_categoria = datos.nombre_categoria

    db.commit()
    db.refresh(categoria)

    return categoria

def eliminar_categoria(id: int, db: Session):
    categoria = obtener_categoria(id, db)

    db.delete(categoria)
    db.commit()

    return {"mensaje": "Categoria eliminada correctamente"}