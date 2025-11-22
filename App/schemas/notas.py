from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import date

class DetalleNotaIngresoBase(BaseModel):
    producto_id: int
    cantidad: int

class DetalleNotaIngresoCreate(DetalleNotaIngresoBase):
    pass

class DetalleNotaIngresoResponse(DetalleNotaIngresoBase):
    id: int
    nota_ingreso_id: int
    model_config = ConfigDict(from_attributes=True)

class NotaIngresoBase(BaseModel):
    proveedor_id: Optional[int] = None
    usuario_id: Optional[int] = None
    fecha: date

class NotaIngresoCreate(BaseModel):
    proveedor_id: Optional[int] = None
    usuario_id: Optional[int] = None
    detalles: List[DetalleNotaIngresoCreate]

class NotaIngresoResponse(NotaIngresoBase):
    id: int
    detalles: Optional[List[DetalleNotaIngresoResponse]] = None
    model_config = ConfigDict(from_attributes=True)


class DetalleNotaSalidaBase(BaseModel):
    producto_id: int
    cantidad: int

class DetalleNotaSalidaCreate(DetalleNotaSalidaBase):
    pass

class DetalleNotaSalidaResponse(DetalleNotaSalidaBase):
    id: int
    nota_salida_id: int
    model_config = ConfigDict(from_attributes=True)

class NotaSalidaBase(BaseModel):
    usuario_id: Optional[int] = None
    motivo: Optional[str] = None
    destino: Optional[str] = None
    fecha: date

class NotaSalidaCreate(BaseModel):
    usuario_id: Optional[int] = None
    motivo: Optional[str] = None
    destino: Optional[str] = None
    detalles: List[DetalleNotaSalidaCreate]

class NotaSalidaResponse(NotaSalidaBase):
    id: int
    detalles: Optional[List[DetalleNotaSalidaResponse]] = None
    model_config = ConfigDict(from_attributes=True)