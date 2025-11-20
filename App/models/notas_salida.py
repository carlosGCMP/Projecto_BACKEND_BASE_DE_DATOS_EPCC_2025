from sqlalchemy import Column, Integer, ForeignKey, String, Date
from sqlalchemy.orm import relationship
from datetime import date
from app.config.database import Base

class NotaSalida(Base):
    __tablename__ = "nota_salida"

    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=True)
    motivo = Column(String(200), nullable=True)
    destino = Column(String(200), nullable=True)
    fecha = Column(Date, nullable=False, default=date.today)

    # Relationships
    usuario = relationship("Usuario", back_populates="notas_salida")
    detalles = relationship("DetalleNotaSalida", back_populates="nota_salida", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<NotaSalida(id={self.id}, fecha='{self.fecha}', motivo='{self.motivo}')>"


class DetalleNotaSalida(Base):
    __tablename__ = "detalle_nota_salida"

    id = Column(Integer, primary_key=True, index=True)
    nota_salida_id = Column(Integer, ForeignKey("nota_salida.id", ondelete="CASCADE"), nullable=False)
    producto_id = Column(Integer, ForeignKey("productos.id"), nullable=False)
    cantidad = Column(Integer, nullable=False)

    # Relationships
    nota_salida = relationship("NotaSalida", back_populates="detalles")
    producto = relationship("Producto", back_populates="detalles_nota_salida")

    def __repr__(self):
        return f"<DetalleNotaSalida(id={self.id}, producto_id={self.producto_id}, cantidad={self.cantidad})>"