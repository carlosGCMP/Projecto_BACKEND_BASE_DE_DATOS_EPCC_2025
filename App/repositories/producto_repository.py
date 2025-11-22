from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.producto import Producto
from app.repositories.base import BaseRepository

class ProductoRepository(BaseRepository[Producto]):
    """Repository especializado para Productos"""
    
    def __init__(self, db: Session):
        super().__init__(db, Producto)
    
    def obtener_por_categoria(self, categoria_id: int, skip: int = 0, limit: int = 100) -> List[Producto]:
        """
        Obtener productos por categoría
        
        Args:
            categoria_id: ID de la categoría
            skip: Saltar N registros
            limit: Limitar a N registros
            
        Returns:
            Lista de productos de la categoría
        """
        return self.db.query(Producto).filter(
            Producto.categoria_id == categoria_id
        ).offset(skip).limit(limit).all()
    
    def obtener_stock_bajo(self, skip: int = 0, limit: int = 100) -> List[Producto]:
        """
        Obtener productos con stock por debajo del mínimo
        
        Args:
            skip: Saltar N registros
            limit: Limitar a N registros
            
        Returns:
            Lista de productos con stock bajo
        """
        return self.db.query(Producto).filter(
            Producto.stock_actual < Producto.stock_min
        ).offset(skip).limit(limit).all()
    
    def obtener_stock_critico(self, skip: int = 0, limit: int = 100) -> List[Producto]:
        """
        Obtener productos sin stock
        
        Args:
            skip: Saltar N registros
            limit: Limitar a N registros
            
        Returns:
            Lista de productos sin stock
        """
        return self.db.query(Producto).filter(
            Producto.stock_actual == 0
        ).offset(skip).limit(limit).all()
    
    def obtener_stock_alto(self, skip: int = 0, limit: int = 100) -> List[Producto]:
        """
        Obtener productos con stock por encima del máximo
        
        Args:
            skip: Saltar N registros
            limit: Limitar a N registros
            
        Returns:
            Lista de productos con stock alto
        """
        return self.db.query(Producto).filter(
            Producto.stock_actual > Producto.stock_max
        ).offset(skip).limit(limit).all()
    
    def actualizar_stock(self, producto_id: int, cantidad: int) -> Optional[Producto]:
        """
        Actualizar el stock de un producto
        
        Args:
            producto_id: ID del producto
            cantidad: Cantidad a sumar (negativa para restar)
            
        Returns:
            Producto actualizado o None
        """
        producto = self.obtener_por_id(producto_id)
        if producto:
            producto.stock_actual += cantidad
            self.db.commit()
            self.db.refresh(producto)
        return producto
    
    def existe_nombre(self, nombre: str, excluir_id: int = None) -> bool:
        """
        Verificar si un nombre de producto ya existe
        
        Args:
            nombre: Nombre del producto
            excluir_id: ID de producto a excluir de la búsqueda
            
        Returns:
            True si existe, False si no
        """
        query = self.db.query(Producto).filter(Producto.nombre == nombre)
        if excluir_id:
            query = query.filter(Producto.id != excluir_id)
        return query.first() is not None