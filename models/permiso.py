from sqlalchemy import String, Column, Integer
from app.database import Base
class Permiso(Base):
    __tablename__="permisos"
    id = Column(Integer,primary_key=True)
    nombre= Column(String, nullable=False, unique=True)