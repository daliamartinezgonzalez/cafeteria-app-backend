from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.bebida import Bebida
from models.categoria import Categoria
from models.ingrediente import Ingrediente
from models.bebida_ingrediente import BebidaIngrediente

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
        
def validar_ingredientes(ingredientes, db: Session):
    ids = [ingrediente.id_ingrediente for ingrediente in ingredientes]
    # se verifica que no se repita un ingrediente
    if len(ids) != len(set(ids)):
        raise HTTPException(
            status_code=400,
            detail="No se puede agregar el mismo ingrediente más de una vez"
        )
    ingredientes_existentes = db.query(Ingrediente).filter(
        Ingrediente.id.in_(ids)
    ).all()
    ids_existentes = {ingrediente.id for ingrediente in ingredientes_existentes}
    # se verifica que todos los ingredientes seleccionados existan
    if not set(ids).issubset(ids_existentes):
        raise HTTPException(
            status_code=404,
            detail="Uno o más ingredientes no existen"
        )

def guardar_ingredientes(bebida_id: int, ingredientes, db: Session):
    validar_ingredientes(ingredientes, db)

    for ingrediente in ingredientes:
        relacion = BebidaIngrediente(
            id_bebida=bebida_id,
            id_ingrediente=ingrediente.id_ingrediente,
            cantidad=ingrediente.cantidad,
            unidad=ingrediente.unidad
        )
        db.add(relacion)

def crear_bebida(datos, db: Session):
    try:
        validar_categoria(datos.id_categoria, db)
        # se separan los ingredientes de los datos de la bebida
        datos_bebida = datos.model_dump(exclude={"ingredientes"})
        ingredientes = datos.ingredientes
        bebida = Bebida(**datos_bebida)
        db.add(bebida)
        db.flush()
        # se guardan los ingredientes relacionados con la bebida
        guardar_ingredientes(bebida.id, ingredientes, db)
        db.commit()
        db.refresh(bebida)
        return bebida
    except Exception:
        db.rollback()
        raise


def editar_bebida(id: int, datos, db: Session):
    try:
        bebida = obtener_bebida(id, db)
        validar_categoria(datos.id_categoria, db)
        # se separan los ingredientes de los datos de la bebida
        datos_bebida = datos.model_dump(exclude={"ingredientes"})
        ingredientes = datos.ingredientes
        # se actualizan todos los campos de la bebida
        for campo, valor in datos_bebida.items():
            setattr(bebida, campo, valor)
        # se eliminan las relaciones anteriores
        db.query(BebidaIngrediente).filter(
            BebidaIngrediente.id_bebida == id
        ).delete(synchronize_session=False)
        # se guardan los nuevos ingredientes
        guardar_ingredientes(id, ingredientes, db)
        db.commit()
        db.refresh(bebida)
        return bebida

    except Exception:
        db.rollback()
        raise

def actualizar_bebida(id: int, datos, db: Session):
    try:
        bebida = obtener_bebida(id, db)
        # se obtienen solamente los campos que fueron enviados
        datos_bebida = datos.model_dump(exclude_unset=True)
        # se separan los ingredientes de los datos de la bebida
        ingredientes = datos_bebida.pop("ingredientes", None)
        # si se quiere cambiar la categoria se verifica que exista
        if "id_categoria" in datos_bebida:
            validar_categoria(datos_bebida["id_categoria"], db)
        # se actualizan unicamente los campos enviados
        for campo, valor in datos_bebida.items():
            setattr(bebida, campo, valor)
        # si se enviaron ingredientes se reemplazan las relaciones anteriores
        if ingredientes is not None:
            db.query(BebidaIngrediente).filter(
                BebidaIngrediente.id_bebida == id
            ).delete(synchronize_session=False)

            guardar_ingredientes(id, ingredientes, db)
        db.commit()
        db.refresh(bebida)
        return bebida

    except Exception:
        db.rollback()
        raise


def eliminar_bebida(id: int, db: Session):
    bebida = obtener_bebida(id, db)
    db.delete(bebida)
    db.commit()
    return {"mensaje": "Bebida eliminada correctamente"}