from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship
from app.database import Base

class Ingrediente(Base):
    __tablename__ = "ingredientes"

    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False, unique=True)

    bebidas = relationship(
        "BebidaIngrediente",
        back_populates="ingrediente"
    )