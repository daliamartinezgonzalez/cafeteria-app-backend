from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.categoria import Categoria
from models.bebida import Bebida

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
    # se verifica si existen bebidas relacionadas con la categoria
    bebidas_asociadas = db.query(Bebida).filter(
        Bebida.id_categoria == id
    ).first()
    if bebidas_asociadas:
        raise HTTPException(
            status_code=409,
            detail="No se puede eliminar la categoría porque tiene bebidas asociadas"
        )
    db.delete(categoria)
    db.commit()
    return {"mensaje": "Categoría eliminada correctamente"}