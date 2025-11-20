from pydantic import BaseModel, ConfigDict
from typing import Optional, List

class RolBase(BaseModel):
    nombre: str

class RolCreate(RolBase):
    pass

class RolUpdate(BaseModel):
    nombre: Optional[str] = None

class RolResponse(RolBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

class RolWithUsuarios(RolResponse):
    usuarios: Optional[List['UsuarioResponse']] = None
    model_config = ConfigDict(from_attributes=True)