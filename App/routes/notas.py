from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.config.database import get_db
from app.models.notas_ingreso import NotaIngreso, DetalleNotaIngreso
from app.models.notas_salida import NotaSalida, DetalleNotaSalida
from app.schemas.notas import (
    NotaIngresoCreate,
    NotaIngresoResponse,
    NotaSalidaCreate,
    NotaSalidaResponse,
)

router = APIRouter()

# ==================== NOTAS DE INGRESO ====================

@router.post("/ingreso/", response_model=NotaIngresoResponse, status_code=status.HTTP_201_CREATED)
def crear_nota_ingreso(nota: NotaIngresoCreate, db: Session = Depends(get_db)):
    """Crear una nota de ingreso"""
    nueva_nota = NotaIngreso(
        proveedor_id=nota.proveedor_id,
        usuario_id=nota.usuario_id,
        fecha=nota.fecha
    )
    
    # Agregar detalles
    for detalle in nota.detalles:
        detalle_obj = DetalleNotaIngreso(
            producto_id=detalle.producto_id,
            cantidad=detalle.cantidad
        )
        nueva_nota.detalles.append(detalle_obj)
    
    db.add(nueva_nota)
    db.commit()
    db.refresh(nueva_nota)
    return nueva_nota

@router.get("/ingreso/", response_model=List[NotaIngresoResponse])
def listar_notas_ingreso(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Listar todas las notas de ingreso"""
    notas = db.query(NotaIngreso).offset(skip).limit(limit).all()
    return notas

@router.get("/ingreso/{nota_id}", response_model=NotaIngresoResponse)
def obtener_nota_ingreso(nota_id: int, db: Session = Depends(get_db)):
    """Obtener una nota de ingreso por ID"""
    nota = db.query(NotaIngreso).filter(NotaIngreso.id == nota_id).first()
    if not nota:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nota de ingreso no encontrada"
        )
    return nota

@router.delete("/ingreso/{nota_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_nota_ingreso(nota_id: int, db: Session = Depends(get_db)):
    """Eliminar una nota de ingreso"""
    nota = db.query(NotaIngreso).filter(NotaIngreso.id == nota_id).first()
    if not nota:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nota de ingreso no encontrada"
        )
    
    db.delete(nota)
    db.commit()
    return None


# ==================== NOTAS DE SALIDA ====================

@router.post("/salida/", response_model=NotaSalidaResponse, status_code=status.HTTP_201_CREATED)
def crear_nota_salida(nota: NotaSalidaCreate, db: Session = Depends(get_db)):
    """Crear una nota de salida"""
    nueva_nota = NotaSalida(
        usuario_id=nota.usuario_id,
        motivo=nota.motivo,
        destino=nota.destino,
        fecha=nota.fecha
    )
    
    # Agregar detalles
    for detalle in nota.detalles:
        detalle_obj = DetalleNotaSalida(
            producto_id=detalle.producto_id,
            cantidad=detalle.cantidad
        )
        nueva_nota.detalles.append(detalle_obj)
    
    db.add(nueva_nota)
    db.commit()
    db.refresh(nueva_nota)
    return nueva_nota

@router.get("/salida/", response_model=List[NotaSalidaResponse])
def listar_notas_salida(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Listar todas las notas de salida"""
    notas = db.query(NotaSalida).offset(skip).limit(limit).all()
    return notas

@router.get("/salida/{nota_id}", response_model=NotaSalidaResponse)
def obtener_nota_salida(nota_id: int, db: Session = Depends(get_db)):
    """Obtener una nota de salida por ID"""
    nota = db.query(NotaSalida).filter(NotaSalida.id == nota_id).first()
    if not nota:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nota de salida no encontrada"
        )
    return nota

@router.delete("/salida/{nota_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_nota_salida(nota_id: int, db: Session = Depends(get_db)):
    """Eliminar una nota de salida"""
    nota = db.query(NotaSalida).filter(NotaSalida.id == nota_id).first()
    if not nota:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nota de salida no encontrada"
        )
    
    db.delete(nota)
    db.commit()
    return None