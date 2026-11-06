from sqlalchemy import Integer, Column, String, ForeignKey, Float
from app.database import Base

class Bebida(Base):
    __tablename__ = "bebidas"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(String, nullable=True)
    precio = Column(Float, nullable=False)
    tamaño = Column(String, nullable=False)
    imagen_url = Column(String, nullable=False)
    id_categoria = Column(Integer, ForeignKey("categorias.id"), nullable=False)