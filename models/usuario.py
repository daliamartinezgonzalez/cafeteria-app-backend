from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    apellido_p = Column(String, nullable=False)
    apellido_m = Column(String, nullable=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    activo = Column(Boolean, default=True)
    id_rol = Column(Integer, ForeignKey("roles.id"), nullable =False)