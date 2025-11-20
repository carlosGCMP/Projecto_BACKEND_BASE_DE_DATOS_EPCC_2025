from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.config.database import get_db
from app.models.proveedor import Proveedor
from app.schemas.proveedor import ProveedorCreate, ProveedorResponse, ProveedorUpdate

router = APIRouter()

@router.post("/", response_model=ProveedorResponse, status_code=status.HTTP_201_CREATED)
def crear_proveedor(proveedor: ProveedorCreate, db: Session = Depends(get_db)):
    """Crear un nuevo proveedor"""
    # Verificar si el RUC ya existe
    if proveedor.ruc:
        db_proveedor = db.query(Proveedor).filter(Proveedor.ruc == proveedor.ruc).first()
        if db_proveedor:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El RUC ya está registrado"
            )
    
    nuevo_proveedor = Proveedor(
        razon_social=proveedor.razon_social,
        ruc=proveedor.ruc,
        telefono=proveedor.telefono,
        direccion=proveedor.direccion,
        correo=proveedor.correo
    )
    
    db.add(nuevo_proveedor)
    db.commit()
    db.refresh(nuevo_proveedor)
    return nuevo_proveedor

@router.get("/", response_model=List[ProveedorResponse])
def listar_proveedores(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Listar todos los proveedores"""
    proveedores = db.query(Proveedor).offset(skip).limit(limit).all()
    return proveedores

@router.get("/{proveedor_id}", response_model=ProveedorResponse)
def obtener_proveedor(proveedor_id: int, db: Session = Depends(get_db)):
    """Obtener un proveedor por ID"""
    proveedor = db.query(Proveedor).filter(Proveedor.id == proveedor_id).first()
    if not proveedor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Proveedor no encontrado"
        )
    return proveedor

@router.put("/{proveedor_id}", response_model=ProveedorResponse)
def actualizar_proveedor(
    proveedor_id: int,
    proveedor_update: ProveedorUpdate,
    db: Session = Depends(get_db)
):
    """Actualizar un proveedor"""
    proveedor = db.query(Proveedor).filter(Proveedor.id == proveedor_id).first()
    if not proveedor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Proveedor no encontrado"
        )
    
    update_data = proveedor_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(proveedor, field, value)
    
    db.commit()
    db.refresh(proveedor)
    return proveedor

@router.delete("/{proveedor_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_proveedor(proveedor_id: int, db: Session = Depends(get_db)):
    """Eliminar un proveedor"""
    proveedor = db.query(Proveedor).filter(Proveedor.id == proveedor_id).first()
    if not proveedor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Proveedor no encontrado"
        )
    
    db.delete(proveedor)
    db.commit()
    return None