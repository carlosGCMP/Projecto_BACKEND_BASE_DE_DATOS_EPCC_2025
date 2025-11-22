import re
from typing import Optional

def validar_username(username: str) -> bool:
    """
    Validar que el username sea válido
    - Mínimo 3 caracteres
    - Máximo 50 caracteres
    - Solo letras, números y guiones bajos
    
    Args:
        username: Username a validar
        
    Returns:
        True si es válido
    """
    if not isinstance(username, str):
        return False
    
    if len(username) < 3 or len(username) > 50:
        return False
    
    # Solo letras, números y guiones bajos
    pattern = r"^[a-zA-Z0-9_]+$"
    return bool(re.match(pattern, username))

def validar_email(email: str) -> bool:
    """
    Validar que el email sea válido
    
    Args:
        email: Email a validar
        
    Returns:
        True si es válido
    """
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

def validar_ruc(ruc: str) -> bool:
    """
    Validar que el RUC sea válido (formato básico)
    - Mínimo 11 dígitos
    
    Args:
        ruc: RUC a validar
        
    Returns:
        True si es válido
    """
    if not isinstance(ruc, str):
        return False
    
    # Solo números
    if not ruc.isdigit():
        return False
    
    # Mínimo 11 dígitos
    return len(ruc) >= 11

def validar_telefono(telefono: str) -> bool:
    """
    Validar que el teléfono sea válido
    - Solo números y símbolos +, -, espacios
    - Mínimo 7 dígitos
    
    Args:
        telefono: Teléfono a validar
        
    Returns:
        True si es válido
    """
    if not isinstance(telefono, str):
        return False
    
    # Solo números, +, -, espacios
    pattern = r"^[\d\s\+\-\(\)]+$"
    if not re.match(pattern, telefono):
        return False
    
    # Contar solo dígitos
    digitos = re.sub(r"\D", "", telefono)
    return len(digitos) >= 7

def validar_stock(stock_actual: int, stock_min: int, stock_max: int) -> bool:
    """
    Validar que los valores de stock sean válidos
    - stock_min <= stock_actual <= stock_max
    - Todos deben ser >= 0
    
    Args:
        stock_actual: Stock actual
        stock_min: Stock mínimo
        stock_max: Stock máximo
        
    Returns:
        True si son válidos
    """
    if stock_actual < 0 or stock_min < 0 or stock_max < 0:
        return False
    
    if stock_min > stock_max:
        return False
    
    if stock_actual < stock_min or stock_actual > stock_max:
        return False
    
    return True

def validar_cantidad(cantidad: int) -> bool:
    """
    Validar que la cantidad sea válida
    - Debe ser mayor a 0
    
    Args:
        cantidad: Cantidad a validar
        
    Returns:
        True si es válida
    """
    return isinstance(cantidad, int) and cantidad > 0