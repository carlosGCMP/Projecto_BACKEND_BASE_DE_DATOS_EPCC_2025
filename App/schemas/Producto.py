from pydantic import BaseModel, ConfigDict, Field
from typing import Optional
from decimal import Decimal

class CategoriaResponse(BaseModel):
    id: int
    nombre: str
    model_config = ConfigDict(from_attributes=True)

class ProductoBase(BaseModel):
    nombre: str
    categoria_id: Optional[int] = None
    stock_actual: int = 0
    stock_min: int = 0
    stock_max: int = 0
    precio: Decimal = Decimal("0.00")

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(BaseModel):
    nombre: Optional[str] = None
    categoria_id: Optional[int] = None
    stock_actual: Optional[int] = None
    stock_min: Optional[int] = None
    stock_max: Optional[int] = None
    precio: Optional[Decimal] = None

class ProductoResponse(ProductoBase):
    id: int
    categoria: Optional[CategoriaResponse] = None
    model_config = ConfigDict(from_attributes=True)

class ProductoStockResponse(ProductoResponse):
    """Información de producto con detalles de stock"""
    stock_disponible: int = Field(description="Stock actual disponible")
    necesita_reorden: bool = Field(description="Si el stock está bajo el mínimo")
    
    @property
    def necesita_reorden(self) -> bool:
        return self.stock_actual < self.stock_min