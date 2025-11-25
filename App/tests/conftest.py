import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

from app.main import app
from app.config.database import Base, get_db

# Base de datos de prueba (SQLite en memoria)
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False}
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    """Override para usar BD de prueba"""
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture()
def db():
    """Fixture para la sesión de BD de prueba"""
    Base.metadata.create_all(bind=engine)
    yield TestingSessionLocal()
    Base.metadata.drop_all(bind=engine)

@pytest.fixture()
def client():
    """Fixture para el cliente de prueba"""
    return TestClient(app)

@pytest.fixture()
def headers():
    """Fixture para headers comunes"""
    return {
        "Content-Type": "application/json"
    }