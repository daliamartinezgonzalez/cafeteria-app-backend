from sqlalchemy import Column, Integer, ForeignKey, Float, String
from app.database import Base

class BebidaIngrediente(Base):
    __tablename__ = "bebida_ingrediente"

    id_bebida = Column(Integer, ForeignKey("bebidas.id"), primary_key=True)
    id_ingrediente = Column(Integer, ForeignKey("ingredientes.id"), primary_key=True)
    cantidad = Column(Float, nullable=False)
    unidad = Column(String(20), nullable=False)