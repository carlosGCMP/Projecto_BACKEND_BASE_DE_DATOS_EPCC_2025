from sqlalchemy import Column, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship
from datetime import date
from app.config.database import Base

class NotaIngreso(Base):
    __tablename__ = "nota_ingreso"

    id = Column(Integer, primary_key=True, index=True)
    proveedor_id = Column(Integer, ForeignKey("proveedores.id"), nullable=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=True)
    fecha = Column(Date, nullable=False, default=date.today)

    # Relationships
    proveedor = relationship("Proveedor", back_populates="notas_ingreso")
    usuario = relationship("Usuario", back_populates="notas_ingreso")
    detalles = relationship("DetalleNotaIngreso", back_populates="nota_ingreso", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<NotaIngreso(id={self.id}, fecha='{self.fecha}')>"


class DetalleNotaIngreso(Base):
    __tablename__ = "detalle_nota_ingreso"

    id = Column(Integer, primary_key=True, index=True)
    nota_ingreso_id = Column(Integer, ForeignKey("nota_ingreso.id", ondelete="CASCADE"), nullable=False)
    producto_id = Column(Integer, ForeignKey("productos.id"), nullable=False)
    cantidad = Column(Integer, nullable=False)

    # Relationships
    nota_ingreso = relationship("NotaIngreso", back_populates="detalles")
    producto = relationship("Producto", back_populates="detalles_nota_ingreso")

    def __repr__(self):
        return f"<DetalleNotaIngreso(id={self.id}, producto_id={self.producto_id}, cantidad={self.cantidad})>"