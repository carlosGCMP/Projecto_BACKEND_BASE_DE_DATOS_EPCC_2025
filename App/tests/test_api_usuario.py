import pytest

def test_crear_usuario(client):
    """Test para crear un usuario"""
    # Crear rol primero
    rol_response = client.post("/api/roles/", json={"nombre": "Usuario"})
    rol_id = rol_response.json()["id"]
    
    # Crear usuario
    usuario_data = {
        "nombre": "Juan Pérez",
        "username": "juanperez",
        "clave": "password123",
        "rol_id": rol_id
    }
    response = client.post("/api/usuarios/", json=usuario_data)
    
    assert response.status_code == 201
    assert response.json()["username"] == "juanperez"
    assert response.json()["nombre"] == "Juan Pérez"

def test_listar_usuarios(client):
    """Test para listar usuarios"""
    # Crear rol y usuario
    rol_response = client.post("/api/roles/", json={"nombre": "Usuario"})
    rol_id = rol_response.json()["id"]
    
    usuario_data = {
        "nombre": "Juan Pérez",
        "username": "juanperez",
        "clave": "password123",
        "rol_id": rol_id
    }
    client.post("/api/usuarios/", json=usuario_data)
    
    # Listar usuarios
    response = client.get("/api/usuarios/")
    
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_obtener_usuario(client):
    """Test para obtener un usuario por ID"""
    # Crear rol y usuario
    rol_response = client.post("/api/roles/", json={"nombre": "Usuario"})
    rol_id = rol_response.json()["id"]
    
    usuario_data = {
        "nombre": "Juan Pérez",
        "username": "juanperez",
        "clave": "password123",
        "rol_id": rol_id
    }
    create_response = client.post("/api/usuarios/", json=usuario_data)
    usuario_id = create_response.json()["id"]
    
    # Obtener usuario
    response = client.get(f"/api/usuarios/{usuario_id}")
    
    assert response.status_code == 200
    assert response.json()["username"] == "juanperez"

def test_actualizar_usuario(client):
    """Test para actualizar un usuario"""
    # Crear rol y usuario
    rol_response = client.post("/api/roles/", json={"nombre": "Usuario"})
    rol_id = rol_response.json()["id"]
    
    usuario_data = {
        "nombre": "Juan Pérez",
        "username": "juanperez",
        "clave": "password123",
        "rol_id": rol_id
    }
    create_response = client.post("/api/usuarios/", json=usuario_data)
    usuario_id = create_response.json()["id"]
    
    # Actualizar usuario
    update_data = {"nombre": "Juan Carlos Pérez"}
    response = client.put(f"/api/usuarios/{usuario_id}", json=update_data)
    
    assert response.status_code == 200
    assert response.json()["nombre"] == "Juan Carlos Pérez"

def test_usuario_duplicado(client):
    """Test para verificar que no se puede crear usuario duplicado"""
    # Crear rol
    rol_response = client.post("/api/roles/", json={"nombre": "Usuario"})
    rol_id = rol_response.json()["id"]
    
    usuario_data = {
        "nombre": "Juan Pérez",
        "username": "juanperez",
        "clave": "password123",
        "rol_id": rol_id
    }
    
    # Crear primer usuario
    client.post("/api/usuarios/", json=usuario_data)
    
    # Intentar crear usuario duplicado
    response = client.post("/api/usuarios/", json=usuario_data)
    
    assert response.status_code == 400
    assert "ya está registrado" in response.json()["detail"]

def test_desactivar_usuario(client):
    """Test para desactivar un usuario"""
    # Crear rol y usuario
    rol_response = client.post("/api/roles/", json={"nombre": "Usuario"})
    rol_id = rol_response.json()["id"]
    
    usuario_data = {
        "nombre": "Juan Pérez",
        "username": "juanperez",
        "clave": "password123",
        "rol_id": rol_id
    }
    create_response = client.post("/api/usuarios/", json=usuario_data)
    usuario_id = create_response.json()["id"]
    
    # Desactivar usuario
    response = client.delete(f"/api/usuarios/{usuario_id}")
    
    assert response.status_code == 204
    
    # Verificar que está inactivo
    get_response = client.get(f"/api/usuarios/{usuario_id}")
    assert get_response.json()["estado"] == False