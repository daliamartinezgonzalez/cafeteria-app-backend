from sqlalchemy import Integer, Column, String
from app.database import Base

class Ingrediente(Base):
    __tablename__="ingredientes"
    id = Column(Integer,primary_key=True)
    nombre = Column(String, nullable=False , unique=True)