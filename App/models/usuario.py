from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.config.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), nullable=False)
    username = Column(String(100), unique=True, nullable=False, index=True)
    clave = Column(Text, nullable=False)
    rol_id = Column(Integer, ForeignKey("roles.id"), nullable=False)
    estado = Column(Boolean, default=True)

    # Relationships
    rol = relationship("Rol", back_populates="usuarios")
    notas_ingreso = relationship("NotaIngreso", back_populates="usuario")
    notas_salida = relationship("NotaSalida", back_populates="usuario")

    def __repr__(self):
        return f"<Usuario(id={self.id}, username='{self.username}')>"