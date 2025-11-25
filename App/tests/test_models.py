import pytest
from app.models.rol import Rol
from app.models.usuario import Usuario
from app.models.categoria import Categoria
from app.models.producto import Producto
from app.utils.security import get_password_hash

def test_crear_rol(db):
    """Test para crear un rol"""
    rol = Rol(nombre="Admin")
    db.add(rol)
    db.commit()
    db.refresh(rol)
    
    assert rol.id is not None
    assert rol.nombre == "Admin"

def test_crear_usuario(db):
    """Test para crear un usuario"""
    # Crear rol primero
    rol = Rol(nombre="Usuario")
    db.add(rol)
    db.commit()
    
    # Crear usuario
    usuario = Usuario(
        nombre="Juan Pérez",
        username="juanperez",
        clave=get_password_hash("password123"),
        rol_id=rol.id
    )
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    
    assert usuario.id is not None
    assert usuario.username == "juanperez"
    assert usuario.estado == True

def test_crear_categoria(db):
    """Test para crear una categoría"""
    categoria = Categoria(nombre="Plásticos")
    db.add(categoria)
    db.commit()
    db.refresh(categoria)
    
    assert categoria.id is not None
    assert categoria.nombre == "Plásticos"

def test_crear_producto(db):
    """Test para crear un producto"""
    # Crear categoría primero
    categoria = Categoria(nombre="Plásticos")
    db.add(categoria)
    db.commit()
    
    # Crear producto
    producto = Producto(
        nombre="Bolsa Plástica 100x200",
        categoria_id=categoria.id,
        stock_actual=500,
        stock_min=100,
        stock_max=1000,
        precio=50.00
    )
    db.add(producto)
    db.commit()
    db.refresh(producto)
    
    assert producto.id is not None
    assert producto.nombre == "Bolsa Plástica 100x200"
    assert producto.stock_actual == 500

def test_stock_bajo(db):
    """Test para verificar stock bajo"""
    categoria = Categoria(nombre="Plásticos")
    db.add(categoria)
    db.commit()
    
    producto = Producto(
        nombre="Producto A",
        categoria_id=categoria.id,
        stock_actual=50,
        stock_min=100,
        stock_max=500,
        precio=10.00
    )
    db.add(producto)
    db.commit()
    db.refresh(producto)
    
    # Verificar que stock_actual < stock_min
    assert producto.stock_actual < producto.stock_min