from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from decimal import Decimal
from datetime import date

class DetalleOrdenCompraBase(BaseModel):
    producto_id: int
    cantidad: int
    precio_unitario: Decimal

class DetalleOrdenCompraCreate(DetalleOrdenCompraBase):
    pass

class DetalleOrdenCompraResponse(DetalleOrdenCompraBase):
    id: int
    orden_id: int
    model_config = ConfigDict(from_attributes=True)

class OrdenCompraBase(BaseModel):
    proveedor_id: int
    fecha: date
    total: Decimal = Decimal("0.00")
    estado: str = "PENDIENTE"

class OrdenCompraCreate(BaseModel):
    proveedor_id: int
    detalles: List[DetalleOrdenCompraCreate]

class OrdenCompraUpdate(BaseModel):
    estado: Optional[str] = None
    total: Optional[Decimal] = None

class ProveedorResponse(BaseModel):
    id: int
    razon_social: str
    model_config = ConfigDict(from_attributes=True)

class OrdenCompraResponse(OrdenCompraBase):
    id: int
    proveedor: Optional[ProveedorResponse] = None
    detalles: Optional[List[DetalleOrdenCompraResponse]] = None
    model_config = ConfigDict(from_attributes=True)