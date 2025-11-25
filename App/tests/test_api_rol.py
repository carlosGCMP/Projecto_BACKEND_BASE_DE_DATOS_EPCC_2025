import pytest
import json

def test_crear_rol(client, headers):
    """Test para crear un rol vía API"""
    data = {"nombre": "Admin"}
    response = client.post("/api/roles/", json=data, headers=headers)
    
    assert response.status_code == 201
    assert response.json()["nombre"] == "Admin"
    assert response.json()["id"] is not None

def test_listar_roles(client):
    """Test para listar roles"""
    # Crear un rol primero
    client.post("/api/roles/", json={"nombre": "Admin"})
    
    response = client.get("/api/roles/")
    
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_obtener_rol(client):
    """Test para obtener un rol por ID"""
    # Crear un rol
    create_response = client.post("/api/roles/", json={"nombre": "Admin"})
    rol_id = create_response.json()["id"]
    
    # Obtener el rol
    response = client.get(f"/api/roles/{rol_id}")
    
    assert response.status_code == 200
    assert response.json()["nombre"] == "Admin"

def test_actualizar_rol(client):
    """Test para actualizar un rol"""
    # Crear un rol
    create_response = client.post("/api/roles/", json={"nombre": "Admin"})
    rol_id = create_response.json()["id"]
    
    # Actualizar el rol
    update_data = {"nombre": "Administrador"}
    response = client.put(f"/api/roles/{rol_id}", json=update_data)
    
    assert response.status_code == 200
    assert response.json()["nombre"] == "Administrador"

def test_eliminar_rol(client):
    """Test para eliminar un rol"""
    # Crear un rol
    create_response = client.post("/api/roles/", json={"nombre": "Admin"})
    rol_id = create_response.json()["id"]
    
    # Eliminar el rol
    response = client.delete(f"/api/roles/{rol_id}")
    
    assert response.status_code == 204
    
    # Verificar que fue eliminado
    get_response = client.get(f"/api/roles/{rol_id}")
    assert get_response.status_code == 404

def test_rol_duplicado(client):
    """Test para verificar que no se puede crear rol duplicado"""
    # Crear primer rol
    client.post("/api/roles/", json={"nombre": "Admin"})
    
    # Intentar crear rol duplicado
    response = client.post("/api/roles/", json={"nombre": "Admin"})
    
    assert response.status_code == 400
    assert "ya existe" in response.json()["detail"]