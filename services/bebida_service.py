from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.bebida import Bebida
from models.categoria import Categoria

def obtener_bebidas(db: Session):
    return db.query(Bebida).all()

def obtener_bebida(id: int, db: Session):
    bebida = db.query(Bebida).filter(Bebida.id == id).first()
    # si no existe la bebida que se esta buscando
    if bebida is None:
        raise HTTPException(
            status_code=404,
            detail="Bebida no encontrada"
        )

    return bebida

def validar_categoria(id_categoria: int, db: Session):
    categoria = db.query(Categoria).filter(
        Categoria.id == id_categoria
    ).first()

    # se verifica que la categoria seleccionada exista
    if categoria is None:
        raise HTTPException(
            status_code=404,
            detail="Categoría no encontrada"
        )

def crear_bebida(datos, db: Session):
    # se verifica que la categoria exista antes de registrar la bebida
    validar_categoria(datos.id_categoria, db)
    datos_bebida = datos.model_dump()
    bebida = Bebida(**datos_bebida)
    db.add(bebida)
    db.commit()
    db.refresh(bebida)

    return bebida

def editar_bebida(id: int, datos, db: Session):
    bebida = obtener_bebida(id, db)
    # se verifica que la nueva categoria exista
    validar_categoria(datos.id_categoria, db)
    datos_bebida = datos.model_dump()
    # se actualizan todos los campos de la bebida
    for campo, valor in datos_bebida.items():
        setattr(bebida, campo, valor)
    db.commit()
    db.refresh(bebida)

    return bebida

def actualizar_bebida(id: int, datos, db: Session):
    bebida = obtener_bebida(id, db)
    # se obtienen solamente los campos que fueron enviados
    datos_bebida = datos.model_dump(exclude_unset=True)
    # si se quiere cambiar la categoria se verifica que exista
    if "id_categoria" in datos_bebida:
        validar_categoria(datos_bebida["id_categoria"], db)
    # se actualizan unicamente los campos enviados
    for campo, valor in datos_bebida.items():
        setattr(bebida, campo, valor)

    db.commit()
    db.refresh(bebida)

    return bebida


def eliminar_bebida(id: int, db: Session):
    bebida = obtener_bebida(id, db)
    db.delete(bebida)
    db.commit()
    return {"mensaje": "Bebida eliminada correctamente"}