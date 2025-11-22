from pydantic import BaseModel, ConfigDict
from typing import Optional

class UsuarioBase(BaseModel):
    nombre: str
    username: str
    rol_id: int

class UsuarioCreate(UsuarioBase):
    clave: str

class UsuarioUpdate(BaseModel):
    nombre: Optional[str] = None
    username: Optional[str] = None
    rol_id: Optional[int] = None
    estado: Optional[bool] = None

class RolResponse(BaseModel):
    id: int
    nombre: str
    model_config = ConfigDict(from_attributes=True)

class UsuarioResponse(UsuarioBase):
    id: int
    estado: bool
    rol: Optional[RolResponse] = None
    model_config = ConfigDict(from_attributes=True)

class UsuarioLogin(BaseModel):
    username: str
    clave: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    usuario: UsuarioResponse