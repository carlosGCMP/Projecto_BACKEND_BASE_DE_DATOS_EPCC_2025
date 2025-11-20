from pydantic import BaseModel, ConfigDict
from typing import Optional, List

class CategoriaBase(BaseModel):
    nombre: str

class CategoriaCreate(CategoriaBase):
    pass

class CategoriaUpdate(BaseModel):
    nombre: Optional[str] = None

class CategoriaResponse(CategoriaBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class CategoriaWithProductos(CategoriaResponse):
    productos: Optional[List['ProductoResponse']] = None
    model_config = ConfigDict(from_attributes=True)