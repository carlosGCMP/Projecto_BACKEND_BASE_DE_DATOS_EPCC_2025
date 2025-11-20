from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from decimal import Decimal

from app.config.database import get_db
from app.models.orden_compra import OrdenCompra, DetalleOrdenCompra
from app.schemas.orden_compra import OrdenCompraCreate, OrdenCompraResponse, OrdenCompraUpdate

router = APIRouter()

@router.post("/", response_model=OrdenCompraResponse, status_code=status.HTTP_201_CREATED)
def crear_orden_compra(orden: OrdenCompraCreate, db: Session = Depends(get_db)):
    """Crear una nueva orden de compra"""
    # Crear la orden
    nueva_orden = OrdenCompra(proveedor_id=orden.proveedor_id)
    
    # Agregar detalles y calcular total
    total = Decimal("0.00")
    for detalle in orden.detalles:
        detalle_obj = DetalleOrdenCompra(
            producto_id=detalle.producto_id,
            cantidad=detalle.cantidad,
            precio_unitario=detalle.precio_unitario
        )
        nueva_orden.detalles.append(detalle_obj)
        total += detalle.precio_unitario * detalle.cantidad
    
    nueva_orden.total = total
    
    db.add(nueva_orden)
    db.commit()
    db.refresh(nueva_orden)
    return nueva_orden

@router.get("/", response_model=List[OrdenCompraResponse])
def listar_ordenes(
    skip: int = 0,
    limit: int = 100,
    estado: str = None,
    db: Session = Depends(get_db)
):
    """Listar órdenes de compra con filtro opcional por estado"""
    query = db.query(OrdenCompra)
    
    if estado:
        query = query.filter(OrdenCompra.estado == estado)
    
    ordenes = query.offset(skip).limit(limit).all()
    return ordenes

@router.get("/{orden_id}", response_model=OrdenCompraResponse)
def obtener_orden(orden_id: int, db: Session = Depends(get_db)):
    """Obtener una orden por ID"""
    orden = db.query(OrdenCompra).filter(OrdenCompra.id == orden_id).first()
    if not orden:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Orden no encontrada"
        )
    return orden

@router.put("/{orden_id}", response_model=OrdenCompraResponse)
def actualizar_orden(
    orden_id: int,
    orden_update: OrdenCompraUpdate,
    db: Session = Depends(get_db)
):
    """Actualizar una orden de compra"""
    orden = db.query(OrdenCompra).filter(OrdenCompra.id == orden_id).first()
    if not orden:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Orden no encontrada"
        )
    
    update_data = orden_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(orden, field, value)
    
    db.commit()
    db.refresh(orden)
    return orden

@router.delete("/{orden_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_orden(orden_id: int, db: Session = Depends(get_db)):
    """Eliminar una orden de compra"""
    orden = db.query(OrdenCompra).filter(OrdenCompra.id == orden_id).first()
    if not orden:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Orden no encontrada"
        )
    
    db.delete(orden)
    db.commit()
    return None