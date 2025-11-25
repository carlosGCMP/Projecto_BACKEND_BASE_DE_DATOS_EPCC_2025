#  Plastitex Backend API

Sistema de gestión de inventario desarrollado con FastAPI, SQLAlchemy y PostgreSQL para la empresa Plastitex.

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115.0-green.svg)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-12+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

---

##  Tablas de Contenidos

- [Características](#-características)
- [Tecnologías](#-tecnologías)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Requisitos Previos](#-requisitos-previos)
- [Instalación](#-instalación)
- [Configuración](#-configuración)
- [Ejecución](#-ejecución)
- [Endpoints API](#-endpoints-api)
- [Base de Datos](#-base-de-datos)
- [Testing](#-testing)
- [Desarrollo](#-desarrollo)
- [Documentación API](#-documentación-api)
- [Integración Frontend](#-integración-frontend)

---

##  Características

-  **API RESTful completa** con 36+ endpoints
-  **Autenticación JWT** con tokens seguros
-  **CRUD completo** para todos los modelos
-  **Validación de datos** con Pydantic
-  **ORM SQLAlchemy** con PostgreSQL
-  **Documentación automática** (Swagger UI + ReDoc)
-  **Tests unitarios** con pytest
-  **Manejo de errores** personalizado
-  **CORS habilitado** para frontend
-  **Seguridad** con hash de contraseñas (bcrypt)
-  **Repositorios** para separación de capas
-  **Validadores** personalizados

---

##  Tecnologías

| Tecnología | Versión | Descripción |
|-----------|---------|-------------|
| **Python** | 3.10+ | Lenguaje de programación |
| **FastAPI** | 0.115.0 | Framework web moderno y rápido |
| **SQLAlchemy** | 2.0.35 | ORM para Python |
| **PostgreSQL** | 12+ | Base de datos relacional |
| **Pydantic** | 2.10.0 | Validación de datos |
| **Uvicorn** | 0.30.0 | Servidor ASGI |
| **python-jose** | 3.3.0 | Manejo de tokens JWT |
| **passlib** | 1.7.4 | Hash de contraseñas |
| **pytest** | 7.4.3 | Framework de testing |
| **psycopg2** | 2.9.11 | Adaptador PostgreSQL |

---

##  Estructura del Proyecto

```
plastitex-backend/
│
├── 📁 app/                          # Aplicación principal
│   ├── __init__.py
│   ├── main.py                      # Punto de entrada FastAPI
│   │
│   ├── 📁 config/                   # Configuración
│   │   ├── __init__.py
│   │   └── database.py              # Conexión PostgreSQL
│   │
│   ├── 📁 models/                   # Modelos SQLAlchemy (ORM)
│   │   ├── __init__.py
│   │   ├── rol.py                   # Modelo Rol
│   │   ├── usuario.py               # Modelo Usuario
│   │   ├── categoria.py             # Modelo Categoría
│   │   ├── producto.py              # Modelo Producto
│   │   ├── proveedor.py             # Modelo Proveedor
│   │   ├── orden_compra.py          # Modelo Orden de Compra
│   │   ├── notas_ingreso.py         # Modelo Nota de Ingreso
│   │   └── notas_salida.py          # Modelo Nota de Salida
│   │
│   ├── 📁 schemas/                  # Schemas Pydantic (Validación)
│   │   ├── __init__.py
│   │   ├── rol.py
│   │   ├── usuario.py
│   │   ├── categoria.py
│   │   ├── producto.py
│   │   ├── proveedor.py
│   │   ├── orden_compra.py
│   │   └── notas.py
│   │
│   ├── 📁 routes/                   # Endpoints API
│   │   ├── __init__.py
│   │   ├── rol.py                   # CRUD Roles
│   │   ├── usuario.py               # CRUD Usuarios
│   │   ├── categoria.py             # CRUD Categorías
│   │   ├── producto.py              # CRUD Productos
│   │   ├── proveedor.py             # CRUD Proveedores
│   │   ├── orden_compra.py          # CRUD Órdenes
│   │   └── notas.py                 # CRUD Notas
│   │
│   ├── 📁 repositories/             # Capa de acceso a datos
│   │   ├── __init__.py
│   │   ├── base.py                  # Repository base
│   │   ├── usuario_repository.py
│   │   └── producto_repository.py
│   │
│   └── 📁 utils/                    # Utilidades
│       ├── __init__.py
│       ├── security.py              # JWT, Hash
│       ├── dependencies.py          # Autenticación
│       ├── exceptions.py            # Excepciones
│       └── validators.py            # Validaciones
│
├── 📁 tests/                        # Tests unitarios
│   ├── __init__.py
│   ├── conftest.py                  # Configuración pytest
│   ├── test_models.py               # Tests modelos
│   ├── test_api_rol.py              # Tests API roles
│   ├── test_api_usuario.py          # Tests API usuarios
│   └── test_utils.py                # Tests utilidades
│
├── .env                             # Variables de entorno
├── .gitignore                       # Archivos ignorados por Git
├── requirements.txt                 # Dependencias Python
├── pytest.ini                       # Configuración pytest
├── README.md                        # Este archivo
└── venv/                            # Entorno virtual
```

---

##  Instalación

### 1. Clonar el repositorio (o descargar)

```bash
git clone <url-del-repositorio>
cd plastitex-backend
```

### 2. Crear entorno virtual

**Windows:**
```powershell
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

##  Configuración

### 1. Crear base de datos PostgreSQL

Abre **pgAdmin** o **psql** y ejecuta:

```sql
CREATE DATABASE plastitex_db;
```

### 2. Configurar variables de entorno

Crea un archivo `.env` en la raíz del proyecto:

```env
# Base de Datos
DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/plastitex_db

# Seguridad JWT
SECRET_KEY=tu-clave-secreta-super-segura-cambiala
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

**⚠️ IMPORTANTE:** Reemplaza:
- `usuario` - Tu usuario de PostgreSQL (por defecto: `postgres`)
- `contraseña` - Tu contraseña de PostgreSQL
- `SECRET_KEY` - Genera una clave segura única

**Generar SECRET_KEY segura:**
```python
import secrets
print(secrets.token_urlsafe(32))
```

### 3. Verificar conexión

```bash
python -c "from app.config.database import engine; print('✅ Conexión exitosa')"
```

---
##  Ejecución

### Modo Desarrollo (con recarga automática)

```bash
uvicorn app.main:app --reload
```

### Modo Producción

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

El servidor estará disponible en:
- **API**: http://localhost:8000
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

## 🔌 Endpoints API

### 🔐 Roles (5 endpoints)
```
POST   /api/roles/              # Crear rol
GET    /api/roles/              # Listar roles
GET    /api/roles/{id}          # Obtener rol
PUT    /api/roles/{id}          # Actualizar rol
DELETE /api/roles/{id}          # Eliminar rol
```

### 👤 Usuarios (5 endpoints)
```
POST   /api/usuarios/           # Crear usuario
GET    /api/usuarios/           # Listar usuarios
GET    /api/usuarios/{id}       # Obtener usuario
PUT    /api/usuarios/{id}       # Actualizar usuario
DELETE /api/usuarios/{id}       # Desactivar usuario
```

### 📂 Categorías (5 endpoints)
```
POST   /api/categorias/         # Crear categoría
GET    /api/categorias/         # Listar categorías
GET    /api/categorias/{id}     # Obtener categoría
PUT    /api/categorias/{id}     # Actualizar categoría
DELETE /api/categorias/{id}     # Eliminar categoría
```

### 📦 Productos (6 endpoints)
```
POST   /api/productos/          # Crear producto
GET    /api/productos/          # Listar productos
GET    /api/productos/stock/bajo # Stock bajo mínimo
GET    /api/productos/{id}      # Obtener producto
PUT    /api/productos/{id}      # Actualizar producto
DELETE /api/productos/{id}      # Eliminar producto
```

### 🏢 Proveedores (5 endpoints)
```
POST   /api/proveedores/        # Crear proveedor
GET    /api/proveedores/        # Listar proveedores
GET    /api/proveedores/{id}    # Obtener proveedor
PUT    /api/proveedores/{id}    # Actualizar proveedor
DELETE /api/proveedores/{id}    # Eliminar proveedor
```

### 📋 Órdenes de Compra (5 endpoints)
```
POST   /api/ordenes/            # Crear orden
GET    /api/ordenes/            # Listar órdenes
GET    /api/ordenes/{id}        # Obtener orden
PUT    /api/ordenes/{id}        # Actualizar orden
DELETE /api/ordenes/{id}        # Eliminar orden
```

### 📝 Notas (4 endpoints)
```
POST   /api/notas/ingreso/      # Crear nota ingreso
GET    /api/notas/ingreso/      # Listar notas ingreso
POST   /api/notas/salida/       # Crear nota salida
GET    /api/notas/salida/       # Listar notas salida
```

**Total: 35 Endpoints REST**

---
### Tablas Implementadas (11)

1. **roles** - Roles de usuario (Admin, Usuario, etc.)
2. **usuarios** - Usuarios del sistema
3. **categorias** - Categorías de productos
4. **productos** - Inventario de productos
5. **proveedores** - Proveedores de la empresa
6. **orden_compra** - Órdenes de compra
7. **detalle_orden_compra** - Detalles de órdenes
8. **nota_ingreso** - Registro de ingresos
9. **detalle_nota_ingreso** - Detalles de ingresos
10. **nota_salida** - Registro de salidas
11. **detalle_nota_salida** - Detalles de salidas

---

##  Testing

### Ejecutar todos los tests

```bash
pytest
```

### Con cobertura de código

```bash
pytest --cov=app tests/
```

### Tests específicos

```bash
# Solo tests de modelos
pytest tests/test_models.py

# Solo tests de API
pytest tests/test_api_rol.py

# Con salida detallada
pytest -v
```

### Cobertura esperada

- **Modelos**: 90%+
- **Schemas**: 95%+
- **Routes**: 85%+
- **Utils**: 90%+

---

##  Desarrollo

### Arquitectura de Capas

El proyecto sigue una **arquitectura en capas** para separación de responsabilidades:

```
┌─────────────────────────────────────┐
│         Routes (API Layer)          │  ← Endpoints FastAPI
├─────────────────────────────────────┤
│       Services (Business Logic)     │  ← Lógica de negocio
├─────────────────────────────────────┤
│     Repositories (Data Access)      │  ← Acceso a datos
├─────────────────────────────────────┤
│        Models (ORM Layer)           │  ← SQLAlchemy Models
├─────────────────────────────────────┤
│         Database (PostgreSQL)       │  ← Base de datos
└─────────────────────────────────────┘
```

### Convenciones de Código

- **PEP 8** para estilo de código Python
- **Type hints** en funciones
- **Docstrings** en clases y funciones importantes
- **Nombres descriptivos** para variables y funciones
- **Separación de responsabilidades**

### Agregar un nuevo modelo

1. Crear modelo en `app/models/`
2. Crear schema en `app/schemas/`
3. Crear router en `app/routes/`
4. Registrar router en `app/main.py`
5. Crear tests en `tests/`

---

##  Documentación API

### Swagger UI (Interactiva)

Accede a: **http://localhost:8000/docs**

Características:
- ✅ Probar endpoints en vivo
- ✅ Ver request/response examples
- ✅ Autenticación JWT
- ✅ Validación de esquemas

### ReDoc (Legible)

Accede a: **http://localhost:8000/redoc**

Características:
- ✅ Documentación clara y organizada
- ✅ Búsqueda de endpoints
- ✅ Exportar a PDF

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT.

---

##  Contribuciones

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama (`git checkout -b feature/nueva-funcionalidad`)
3. Commit cambios (`git commit -m 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

---

## Contacto

Para preguntas o soporte, contacta a: [cgutierrezca@unsa.edu.pe]

---
