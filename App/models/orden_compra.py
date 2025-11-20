from sqlalchemy import Column, Integer, ForeignKey, Numeric, String, Date
from sqlalchemy.orm import relationship
from datetime import date
from app.config.database import Base

class OrdenCompra(Base):
    __tablename__ = "orden_compra"

    id = Column(Integer, primary_key=True, index=True)
    proveedor_id = Column(Integer, ForeignKey("proveedores.id"), nullable=False)
    fecha = Column(Date, nullable=False, default=date.today)
    total = Column(Numeric(10, 2), default=0)
    estado = Column(String(20), default="PENDIENTE")

    # Relationships
    proveedor = relationship("Proveedor", back_populates="ordenes_compra")
    detalles = relationship("DetalleOrdenCompra", back_populates="orden", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<OrdenCompra(id={self.id}, proveedor_id={self.proveedor_id}, estado='{self.estado}')>"


class DetalleOrdenCompra(Base):
    __tablename__ = "detalle_orden_compra"

    id = Column(Integer, primary_key=True, index=True)
    orden_id = Column(Integer, ForeignKey("orden_compra.id", ondelete="CASCADE"), nullable=False)
    producto_id = Column(Integer, ForeignKey("productos.id"), nullable=False)
    cantidad = Column(Integer, nullable=False)
    precio_unitario = Column(Numeric(10, 2), nullable=False)

    # Relationships
    orden = relationship("OrdenCompra", back_populates="detalles")
    producto = relationship("Producto", back_populates="detalles_orden_compra")

    def __repr__(self):
        return f"<DetalleOrdenCompra(id={self.id}, producto_id={self.producto_id}, cantidad={self.cantidad})>"