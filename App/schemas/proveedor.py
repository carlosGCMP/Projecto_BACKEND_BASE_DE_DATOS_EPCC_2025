from pydantic import BaseModel, ConfigDict
from typing import Optional, List

class ProveedorBase(BaseModel):
    razon_social: str
    ruc: Optional[str] = None
    telefono: Optional[str] = None
    direccion: Optional[str] = None
    correo: Optional[str] = None

class ProveedorCreate(ProveedorBase):
    pass

class ProveedorUpdate(BaseModel):
    razon_social: Optional[str] = None
    ruc: Optional[str] = None
    telefono: Optional[str] = None
    direccion: Optional[str] = None
    correo: Optional[str] = None

class ProveedorResponse(ProveedorBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class ProveedorWithOrdenes(ProveedorResponse):
    ordenes_compra: Optional[List['OrdenCompraResponse']] = None
    model_config = ConfigDict(from_attributes=True)