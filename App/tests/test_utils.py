import pytest
from app.utils.security import (
    get_password_hash,
    verify_password,
    create_access_token,
    decode_access_token,
)
from app.utils.validators import (
    validar_username,
    validar_email,
    validar_ruc,
    validar_telefono,
    validar_stock,
    validar_cantidad,
)

# ==================== Tests Security ====================

def test_hash_password():
    """Test para hashear contraseña"""
    password = "mi_contraseña_segura_123"
    hashed = get_password_hash(password)
    
    assert hashed != password
    assert len(hashed) > 0

def test_verify_password():
    """Test para verificar contraseña"""
    password = "mi_contraseña_segura_123"
    hashed = get_password_hash(password)
    
    assert verify_password(password, hashed) == True
    assert verify_password("contraseña_incorrecta", hashed) == False

def test_create_access_token():
    """Test para crear token JWT"""
    data = {"sub": "1", "username": "testuser"}
    token = create_access_token(data)
    
    assert token is not None
    assert len(token) > 0
    assert isinstance(token, str)

def test_decode_access_token():
    """Test para decodificar token JWT"""
    data = {"sub": "1", "username": "testuser"}
    token = create_access_token(data)
    decoded = decode_access_token(token)
    
    assert decoded is not None
    assert decoded["sub"] == "1"
    assert decoded["username"] == "testuser"

def test_decode_invalid_token():
    """Test para decodificar token inválido"""
    invalid_token = "token.invalido.aqui"
    decoded = decode_access_token(invalid_token)
    
    assert decoded is None

# ==================== Tests Validators ====================

def test_validar_username_valido():
    """Test para validar username válido"""
    assert validar_username("juan123") == True
    assert validar_username("usuario_test") == True
    assert validar_username("admin") == True

def test_validar_username_invalido():
    """Test para validar username inválido"""
    assert validar_username("ab") == False  # Muy corto
    assert validar_username("usuario@123") == False  # Caracteres inválidos
    assert validar_username("") == False  # Vacío

def test_validar_email_valido():
    """Test para validar email válido"""
    assert validar_email("usuario@example.com") == True
    assert validar_email("test.user@domain.co.uk") == True

def test_validar_email_invalido():
    """Test para validar email inválido"""
    assert validar_email("usuario@") == False
    assert validar_email("usuario.com") == False
    assert validar_email("") == False

def test_validar_ruc_valido():
    """Test para validar RUC válido"""
    assert validar_ruc("12345678901") == True
    assert validar_ruc("20123456789") == True

def test_validar_ruc_invalido():
    """Test para validar RUC inválido"""
    assert validar_ruc("123") == False  # Muy corto
    assert validar_ruc("abc12345678") == False  # Contiene letras
    assert validar_ruc("") == False

def test_validar_telefono_valido():
    """Test para validar teléfono válido"""
    assert validar_telefono("9123456789") == True
    assert validar_telefono("+51-912-345-6789") == True
    assert validar_telefono("(912) 3456789") == True

def test_validar_telefono_invalido():
    """Test para validar teléfono inválido"""
    assert validar_telefono("123") == False  # Muy corto
    assert validar_telefono("") == False

def test_validar_stock_valido():
    """Test para validar stock válido"""
    assert validar_stock(500, 100, 1000) == True
    assert validar_stock(0, 0, 100) == True

def test_validar_stock_invalido():
    """Test para validar stock inválido"""
    assert validar_stock(50, 100, 1000) == False  # stock_actual < stock_min
    assert validar_stock(500, 1000, 100) == False  # stock_min > stock_max
    assert validar_stock(-10, 0, 100) == False  # Valor negativo

def test_validar_cantidad_valida():
    """Test para validar cantidad válida"""
    assert validar_cantidad(1) == True
    assert validar_cantidad(100) == True
    assert validar_cantidad(9999) == True

def test_validar_cantidad_invalida():
    """Test para validar cantidad inválida"""
    assert validar_cantidad(0) == False
    assert validar_cantidad(-5) == False