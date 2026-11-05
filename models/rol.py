from sqlalchemy import Column, Integer, String

from app.database import Base
class Rol(Base):
    __tablename__ = "roles"
    id = Column(Integer , primary_key=True)
    nombre = Column(String , nullable=False , unique=True)
    