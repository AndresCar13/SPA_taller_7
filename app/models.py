from sqlalchemy import Column, Integer, String
from config import Base

class tipodocumento(Base):
    __tablename__ ="tipodocumento"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    descripcion = Column(String)