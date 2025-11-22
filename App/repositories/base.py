from typing import TypeVar, Generic, List, Optional, Type
from sqlalchemy.orm import Session
from app.config.database import Base

T = TypeVar('T', bound=Base)

class BaseRepository(Generic[T]):
    """
    Clase base para todos los repositories
    Proporciona métodos CRUD comunes
    """
    
    def __init__(self, db: Session, model: Type[T]):
        self.db = db
        self.model = model
    
    def crear(self, obj_in: dict) -> T:
        """
        Crear un nuevo objeto
        
        Args:
            obj_in: Diccionario con los datos
            
        Returns:
            Objeto creado
        """
        db_obj = self.model(**obj_in)
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj
    
    def obtener_por_id(self, id: int) -> Optional[T]:
        """
        Obtener un objeto por ID
        
        Args:
            id: ID del objeto
            
        Returns:
            Objeto encontrado o None
        """
        return self.db.query(self.model).filter(self.model.id == id).first()
    
    def obtener_todos(self, skip: int = 0, limit: int = 100) -> List[T]:
        """
        Obtener todos los objetos con paginación
        
        Args:
            skip: Saltar N registros
            limit: Limitar a N registros
            
        Returns:
            Lista de objetos
        """
        return self.db.query(self.model).offset(skip).limit(limit).all()
    
    def actualizar(self, id: int, obj_in: dict) -> Optional[T]:
        """
        Actualizar un objeto
        
        Args:
            id: ID del objeto
            obj_in: Diccionario con los datos a actualizar
            
        Returns:
            Objeto actualizado o None
        """
        db_obj = self.obtener_por_id(id)
        if db_obj:
            for field, value in obj_in.items():
                setattr(db_obj, field, value)
            self.db.commit()
            self.db.refresh(db_obj)
        return db_obj
    
    def eliminar(self, id: int) -> bool:
        """
        Eliminar un objeto
        
        Args:
            id: ID del objeto
            
        Returns:
            True si se eliminó, False si no existe
        """
        db_obj = self.obtener_por_id(id)
        if db_obj:
            self.db.delete(db_obj)
            self.db.commit()
            return True
        return False
    
    def existe(self, id: int) -> bool:
        """
        Verificar si un objeto existe
        
        Args:
            id: ID del objeto
            
        Returns:
            True si existe, False si no
        """
        return self.db.query(self.model).filter(self.model.id == id).first() is not None
    
    def contar(self) -> int:
        """
        Contar la cantidad total de objetos
        
        Returns:
            Cantidad de objetos
        """
        return self.db.query(self.model).count()