from typing import Optional
from sqlalchemy.orm import Session
from app.models.usuario import Usuario
from app.repositories.base import BaseRepository
from app.utils.security import get_password_hash

class UsuarioRepository(BaseRepository[Usuario]):
    """Repository especializado para Usuarios"""
    
    def __init__(self, db: Session):
        super().__init__(db, Usuario)
    
    def obtener_por_username(self, username: str) -> Optional[Usuario]:
        """
        Obtener usuario por username
        
        Args:
            username: Username del usuario
            
        Returns:
            Usuario encontrado o None
        """
        return self.db.query(Usuario).filter(Usuario.username == username).first()
    
    def obtener_activos(self, skip: int = 0, limit: int = 100):
        """
        Obtener solo usuarios activos
        
        Args:
            skip: Saltar N registros
            limit: Limitar a N registros
            
        Returns:
            Lista de usuarios activos
        """
        return self.db.query(Usuario).filter(
            Usuario.estado == True
        ).offset(skip).limit(limit).all()
    
    def obtener_por_rol(self, rol_id: int, skip: int = 0, limit: int = 100):
        """
        Obtener usuarios por rol
        
        Args:
            rol_id: ID del rol
            skip: Saltar N registros
            limit: Limitar a N registros
            
        Returns:
            Lista de usuarios del rol
        """
        return self.db.query(Usuario).filter(
            Usuario.rol_id == rol_id
        ).offset(skip).limit(limit).all()
    
    def crear_usuario(self, nombre: str, username: str, clave: str, rol_id: int) -> Usuario:
        """
        Crear un nuevo usuario con contraseña hasheada
        
        Args:
            nombre: Nombre del usuario
            username: Username único
            clave: Contraseña en texto plano
            rol_id: ID del rol
            
        Returns:
            Usuario creado
        """
        usuario = Usuario(
            nombre=nombre,
            username=username,
            clave=get_password_hash(clave),
            rol_id=rol_id
        )
        self.db.add(usuario)
        self.db.commit()
        self.db.refresh(usuario)
        return usuario
    
    def desactivar_usuario(self, usuario_id: int) -> Optional[Usuario]:
        """
        Desactivar un usuario (soft delete)
        
        Args:
            usuario_id: ID del usuario
            
        Returns:
            Usuario actualizado o None
        """
        usuario = self.obtener_por_id(usuario_id)
        if usuario:
            usuario.estado = False
            self.db.commit()
            self.db.refresh(usuario)
        return usuario
    
    def activar_usuario(self, usuario_id: int) -> Optional[Usuario]:
        """
        Activar un usuario
        
        Args:
            usuario_id: ID del usuario
            
        Returns:
            Usuario actualizado o None
        """
        usuario = self.obtener_por_id(usuario_id)
        if usuario:
            usuario.estado = True
            self.db.commit()
            self.db.refresh(usuario)
        return usuario
    
    def existe_username(self, username: str, excluir_id: int = None) -> bool:
        """
        Verificar si un username ya existe
        
        Args:
            username: Username a verificar
            excluir_id: ID de usuario a excluir de la búsqueda
            
        Returns:
            True si existe, False si no
        """
        query = self.db.query(Usuario).filter(Usuario.username == username)
        if excluir_id:
            query = query.filter(Usuario.id != excluir_id)
        return query.first() is not None