from sqlalchemy import Integer, Column, String
from app.database import Base

class Categoria(Base):
    __tablename__="categorias"
    id = Column(Integer,primary_key=True)
    nombre_categoria = Column(String, nullable=False , unique=True)