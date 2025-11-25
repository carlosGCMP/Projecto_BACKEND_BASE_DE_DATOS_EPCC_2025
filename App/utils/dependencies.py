from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.models.usuario import Usuario
from app.utils.security import decode_access_token

security = HTTPBearer()

def get_current_user(
    token: str = Depends(security),
    db: Session = Depends(get_db)
) -> Usuario:
    """
    Dependencia para obtener el usuario actual desde el token JWT
    
    Args:
        token: Token JWT Bearer
        db: Sesión de la base de datos
        
    Returns:
        Usuario autenticado
        
    Raises:
        HTTPException: Si el token es inválido o expiró
    """
    # Obtener el token (HTTPBearer ya retorna el token directamente)
    if hasattr(token, 'credentials'):
        token_str = token.credentials
    else:
        token_str = token
    
    # Decodificar token
    payload = decode_access_token(token_str)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Obtener usuario_id del token
    usuario_id = payload.get("sub")
    if not usuario_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Buscar usuario en BD
    usuario = db.query(Usuario).filter(Usuario.id == int(usuario_id)).first()
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario no encontrado",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Verificar que el usuario está activo
    if not usuario.estado:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Usuario desactivado",
        )
    
    return usuario

def get_current_active_user(
    current_user: Usuario = Depends(get_current_user),
) -> Usuario:
    """
    Dependencia para obtener un usuario activo
    
    Args:
        current_user: Usuario actual del token
        
    Returns:
        Usuario activo
    """
    if not current_user.estado:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Usuario inactivo"
        )
    return current_user