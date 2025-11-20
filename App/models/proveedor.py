from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.config.database import Base

class Proveedor(Base):
    __tablename__ = "proveedores"

    id = Column(Integer, primary_key=True, index=True)
    razon_social = Column(String(150), nullable=False)
    ruc = Column(String(15), unique=True, nullable=True)
    telefono = Column(String(20), nullable=True)
    direccion = Column(Text, nullable=True)
    correo = Column(String(100), nullable=True)

    # Relationships
    ordenes_compra = relationship("OrdenCompra", back_populates="proveedor")
    notas_ingreso = relationship("NotaIngreso", back_populates="proveedor")

    def __repr__(self):
        return f"<Proveedor(id={self.id}, razon_social='{self.razon_social}')>"