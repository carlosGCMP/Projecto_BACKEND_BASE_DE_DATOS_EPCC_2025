from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.config.database import get_db
from app.models.rol import Rol
from app.schemas.rol import RolCreate, RolResponse, RolUpdate

router = APIRouter()

@router.post("/", response_model=RolResponse, status_code=status.HTTP_201_CREATED)
def crear_rol(rol: RolCreate, db: Session = Depends(get_db)):
    """Crear un nuevo rol"""
    db_rol = db.query(Rol).filter(Rol.nombre == rol.nombre).first()
    if db_rol:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El rol ya existe"
        )
    
    nuevo_rol = Rol(nombre=rol.nombre)
    db.add(nuevo_rol)
    db.commit()
    db.refresh(nuevo_rol)
    return nuevo_rol

@router.get("/", response_model=List[RolResponse])
def listar_roles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Listar todos los roles"""
    roles = db.query(Rol).offset(skip).limit(limit).all()
    return roles

@router.get("/{rol_id}", response_model=RolResponse)
def obtener_rol(rol_id: int, db: Session = Depends(get_db)):
    """Obtener un rol por ID"""
    rol = db.query(Rol).filter(Rol.id == rol_id).first()
    if not rol:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Rol no encontrado"
        )
    return rol

@router.put("/{rol_id}", response_model=RolResponse)
def actualizar_rol(rol_id: int, rol_update: RolUpdate, db: Session = Depends(get_db)):
    """Actualizar un rol"""
    rol = db.query(Rol).filter(Rol.id == rol_id).first()
    if not rol:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Rol no encontrado"
        )
    
    update_data = rol_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(rol, field, value)
    
    db.commit()
    db.refresh(rol)
    return rol

@router.delete("/{rol_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_rol(rol_id: int, db: Session = Depends(get_db)):
    """Eliminar un rol"""
    rol = db.query(Rol).filter(Rol.id == rol_id).first()
    if not rol:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Rol no encontrado"
        )
    
    db.delete(rol)
    db.commit()
    return None