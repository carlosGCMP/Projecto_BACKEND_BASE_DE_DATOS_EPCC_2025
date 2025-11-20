from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config.database import engine, Base

# Importar todos los modelos para crear las tablas
from app.models.rol import Rol
from app.models.usuario import Usuario
from app.models.categoria import Categoria
from app.models.producto import Producto
from app.models.proveedor import Proveedor
from app.models.orden_compra import OrdenCompra, DetalleOrdenCompra
from app.models.notas_ingreso import NotaIngreso, DetalleNotaIngreso
from app.models.notas_salida import NotaSalida, DetalleNotaSalida

# Crear las tablas
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Plastitex API",
    description="Sistema de gestión de inventario para Plastitex",
    version="1.0.0"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especificar dominios
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Importar y registrar routers
from app.routes import rol, usuario, categoria, producto, proveedor, orden_compra, notas

app.include_router(rol.router, prefix="/api/roles", tags=["Roles"])
app.include_router(usuario.router, prefix="/api/usuarios", tags=["Usuarios"])
app.include_router(categoria.router, prefix="/api/categorias", tags=["Categorías"])
app.include_router(producto.router, prefix="/api/productos", tags=["Productos"])
app.include_router(proveedor.router, prefix="/api/proveedores", tags=["Proveedores"])
app.include_router(orden_compra.router, prefix="/api/ordenes", tags=["Órdenes de Compra"])
app.include_router(notas.router, prefix="/api/notas", tags=["Notas"])

@app.get("/")
def root():
    return {
        "message": "Plastitex API",
        "version": "1.0.0",
        "status": "active"
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)