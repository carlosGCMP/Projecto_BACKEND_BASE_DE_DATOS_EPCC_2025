from fastapi import HTTPException, status

class UsuarioNoEncontrado(HTTPException):
    """Excepción cuando no se encuentra un usuario"""
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )

class UsuarioYaExiste(HTTPException):
    """Excepción cuando intenta crear un usuario que ya existe"""
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El usuario ya existe"
        )

class CredencialesInvalidas(HTTPException):
    """Excepción cuando las credenciales son inválidas"""
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas",
            headers={"WWW-Authenticate": "Bearer"},
        )

class NoAutorizado(HTTPException):
    """Excepción cuando el usuario no tiene permisos"""
    def __init__(self, detail: str = "No tiene permisos para realizar esta acción"):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=detail
        )

class RecursoNoEncontrado(HTTPException):
    """Excepción genérica cuando no se encuentra un recurso"""
    def __init__(self, recurso: str):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{recurso} no encontrado"
        )

class ErrorConflicto(HTTPException):
    """Excepción cuando hay conflicto en los datos"""
    def __init__(self, detail: str):
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail=detail
        )