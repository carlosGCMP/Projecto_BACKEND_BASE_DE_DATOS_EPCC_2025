from app.schemas.rol import RolCreate, RolResponse, RolUpdate
from app.schemas.usuario import (
    UsuarioCreate,
    UsuarioResponse,
    UsuarioUpdate,
    UsuarioLogin,
    TokenResponse,
)
from app.schemas.categoria import (
    CategoriaCreate,
    CategoriaResponse,
    CategoriaUpdate,
)
from app.schemas.producto import (
    ProductoCreate,
    ProductoResponse,
    ProductoUpdate,
)
from app.schemas.proveedor import (
    ProveedorCreate,
    ProveedorResponse,
    ProveedorUpdate,
)
from app.schemas.orden_compra import (
    OrdenCompraCreate,
    OrdenCompraResponse,
    OrdenCompraUpdate,
    DetalleOrdenCompraCreate,
    DetalleOrdenCompraResponse,
)
from app.schemas.notas import (
    NotaIngresoCreate,
    NotaIngresoResponse,
    DetalleNotaIngresoCreate,
    DetalleNotaIngresoResponse,
    NotaSalidaCreate,
    NotaSalidaResponse,
    DetalleNotaSalidaCreate,
    DetalleNotaSalidaResponse,
)

__all__ = [
    # Rol
    "RolCreate",
    "RolResponse",
    "RolUpdate",
    # Usuario
    "UsuarioCreate",
    "UsuarioResponse",
    "UsuarioUpdate",
    "UsuarioLogin",
    "TokenResponse",
    # Categoria
    "CategoriaCreate",
    "CategoriaResponse",
    "CategoriaUpdate",
    # Producto
    "ProductoCreate",
    "ProductoResponse",
    "ProductoUpdate",
    # Proveedor
    "ProveedorCreate",
    "ProveedorResponse",
    "ProveedorUpdate",
    # Orden Compra
    "OrdenCompraCreate",
    "OrdenCompraResponse",
    "OrdenCompraUpdate",
    "DetalleOrdenCompraCreate",
    "DetalleOrdenCompraResponse",
    # Notas
    "NotaIngresoCreate",
    "NotaIngresoResponse",
    "DetalleNotaIngresoCreate",
    "DetalleNotaIngresoResponse",
    "NotaSalidaCreate",
    "NotaSalidaResponse",
    "DetalleNotaSalidaCreate",
    "DetalleNotaSalidaResponse",
]