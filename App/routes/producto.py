from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.config.database import get_db
from app.models.producto import Producto
from app.schemas.producto import ProductoCreate, ProductoResponse, ProductoUpdate

router = APIRouter()

@router.post("/", response_model=ProductoResponse, status_code=status.HTTP_201_CREATED)
def crear_producto(producto: ProductoCreate, db: Session = Depends(get_db)):
    """Crear un nuevo producto"""
    nuevo_producto = Producto(
        nombre=producto.nombre,
        categoria_id=producto.categoria_id,
        stock_actual=producto.stock_actual,
        stock_min=producto.stock_min,
        stock_max=producto.stock_max,
        precio=producto.precio
    )
    
    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)
    return nuevo_producto

@router.get("/", response_model=List[ProductoResponse])
def listar_productos(
    skip: int = 0,
    limit: int = 100,
    categoria_id: int = None,
    db: Session = Depends(get_db)
):
    """Listar productos con filtro opcional por categoría"""
    query = db.query(Producto)
    
    if categoria_id:
        query = query.filter(Producto.categoria_id == categoria_id)
    
    productos = query.offset(skip).limit(limit).all()
    return productos

@router.get("/stock/bajo", response_model=List[ProductoResponse])
def productos_stock_bajo(db: Session = Depends(get_db)):
    """Obtener productos con stock por debajo del mínimo"""
    productos = db.query(Producto).filter(
        Producto.stock_actual < Producto.stock_min
    ).all()
    return productos

@router.get("/{producto_id}", response_model=ProductoResponse)
def obtener_producto(producto_id: int, db: Session = Depends(get_db)):
    """Obtener un producto por ID"""
    producto = db.query(Producto).filter(Producto.id == producto_id).first()
    if not producto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no encontrado"
        )
    return producto

@router.put("/{producto_id}", response_model=ProductoResponse)
def actualizar_producto(
    producto_id: int,
    producto_update: ProductoUpdate,
    db: Session = Depends(get_db)
):
    """Actualizar un producto"""
    producto = db.query(Producto).filter(Producto.id == producto_id).first()
    if not producto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no encontrado"
        )
    
    update_data = producto_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(producto, field, value)
    
    db.commit()
    db.refresh(producto)
    return producto

@router.delete("/{producto_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_producto(producto_id: int, db: Session = Depends(get_db)):
    """Eliminar un producto"""
    producto = db.query(Producto).filter(Producto.id == producto_id).first()
    if not producto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no encontrado"
        )
    
    db.delete(producto)
    db.commit()
    return None