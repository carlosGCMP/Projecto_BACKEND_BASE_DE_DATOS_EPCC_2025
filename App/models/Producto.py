from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, Index
from sqlalchemy.orm import relationship
from app.config.database import Base

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(150), nullable=False)
    categoria_id = Column(Integer, ForeignKey("categorias.id"))
    stock_actual = Column(Integer, default=0)
    stock_min = Column(Integer, default=0)
    stock_max = Column(Integer, default=0)
    precio = Column(Numeric(10, 2), default=0)

    # Relationships
    categoria = relationship("Categoria", back_populates="productos")
    detalles_orden_compra = relationship("DetalleOrdenCompra", back_populates="producto")
    detalles_nota_ingreso = relationship("DetalleNotaIngreso", back_populates="producto")
    detalles_nota_salida = relationship("DetalleNotaSalida", back_populates="producto")

    # Index
    __table_args__ = (
        Index('idx_productos_categoria', 'categoria_id'),
    )

    def __repr__(self):
        return f"<Producto(id={self.id}, nombre='{self.nombre}', stock={self.stock_actual})>"