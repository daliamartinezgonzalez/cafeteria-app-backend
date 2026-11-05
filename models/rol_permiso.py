from sqlalchemy import Column,Integer, ForeignKey
from app.database import Base
class RolPermiso(Base):
    __tablename__ = "rol_permiso"
    
    id_rol = Column(Integer, ForeignKey("roles.id"), primary_key=True)
    id_permiso = Column(Integer, ForeignKey("permisos.id"), primary_key=True)