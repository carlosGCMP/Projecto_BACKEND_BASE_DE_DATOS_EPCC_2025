import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Cargar variables de entorno
from dotenv import load_dotenv
load_dotenv()

# Obtener la URL de la base de datos
DATABASE_URL = os.getenv("DATABASE_URL")

# Valores por defecto si no está en .env
if not DATABASE_URL:
    DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/plastitex_db"
    print("⚠️ DATABASE_URL no encontrada, usando valor por defecto")

print(f"🔌 Conectando a BD...")

# Crear el engine
try:
    engine = create_engine(
        DATABASE_URL,
        pool_pre_ping=True,
        pool_size=10,
        max_overflow=20,
        echo=False
    )
    print("✅ Engine creado exitosamente")
except Exception as e:
    print(f"❌ Error al crear engine: {e}")
    raise

# Crear la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos
Base = declarative_base()

def get_db():
    """Dependency para obtener sesión de DB"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()