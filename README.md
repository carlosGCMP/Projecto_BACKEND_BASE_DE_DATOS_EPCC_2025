# Primer Dia de Analisis del projecto 8/11/2025
## Descripcion del Analisis 
- Herramienta de modelado **IBM RATIONAL ROSE**
- Base de Datos MYSQL pero se usara **POSTGRESQL**
- Leer el punto *2.3.2* para entender el *MVC*
- Leer el punto *4.4* para poder entender el aplicamiento de datos estadisticos en el proyecto ~~NO IMPORTANTE~~
### **IMPORTANTE**
- Leer el punto *5.6.5* para entenderl el **IBM RATIONAL ROSE**
- **LEER EL PUNTO 5.7.3 PARA REALIZAR LOS MODELOS LOGICOS Y MODELOS FISICOS**
# Segundo Dia de Analisis del Projecto 9/11/2025
## Describcion del Analisis

plastitex_backend/
│
├── app/
│   │
│   ├── main.py                         # Punto de entrada de FastAPI
│   ├── database.py                     # Configuración PostgreSQL + SessionLocal
│   ├── config.py                       # Variables de entorno (JWT, DB URL)
│   │
│   ├── models/                         # ORM (SQLAlchemy)
│   │   ├── usuario.py
│   │   ├── rol.py
│   │   ├── categoria.py
│   │   ├── producto.py
│   │   ├── proveedor.py
│   │   ├── orden_compra.py
│   │   ├── detalle_orden_compra.py
│   │   ├── nota_ingreso.py
│   │   ├── detalle_nota_ingreso.py
│   │   ├── nota_salida.py
│   │   ├── detalle_nota_salida.py
│   │   └── __init__.py
│   │
│   ├── schemas/                        # Pydantic (validaciones)
│   │   ├── usuario.py
│   │   ├── rol.py
│   │   ├── categoria.py
│   │   ├── producto.py
│   │   ├── proveedor.py
│   │   ├── orden_compra.py
│   │   ├── nota_ingreso.py
│   │   ├── nota_salida.py
│   │   └── __init__.py
│   │
│   ├── routers/                        # Endpoints (controladores)
│   │   ├── auth.py
│   │   ├── usuarios.py
│   │   ├── categorias.py
│   │   ├── productos.py
│   │   ├── proveedores.py
│   │   ├── ordenes.py
│   │   ├── notas_ingreso.py
│   │   ├── notas_salida.py
│   │   └── __init__.py
│   │
│   ├── services/                       # Lógica de negocio (opcional)
│   │   ├── auth_service.py
│   │   ├── inventario_service.py
│   │   └── compras_service.py
│   │
│   ├── utils/                          # Utilidades generales
│   │   ├── security.py                 # JWT, hashing
│   │   ├── helpers.py                  # Funciones comunes
│   │   └── pagination.py
│   │
│   └── __init__.py
│
├── migrations/                         # Alembic (migraciones)
│
├── tests/                              # Pruebas automáticas (pytest)
│   ├── test_productos.py
│   └── test_auth.py
│
├── .env                                # Variables de entorno
├── requirements.txt
├── README.md
└── run.sh                              # Script para ejecutar el servidor (opcional)

    