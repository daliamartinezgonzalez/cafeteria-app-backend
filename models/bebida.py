from sqlalchemy import Integer, Column, String, ForeignKey, Float
from sqlalchemy.orm import relationship
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

    categoria = relationship("Categoria")
    ingredientes = relationship(
        "BebidaIngrediente",
        back_populates="bebida",
        cascade="all, delete-orphan"
    )