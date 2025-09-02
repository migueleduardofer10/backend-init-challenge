from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from core.config import settings

# --- Motor de base de datos ---
engine = create_engine(settings.DATABASE_URL)

# --- Sesión de conexión ---
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# --- Base para modelos ---
Base = declarative_base()

# --- Obtener sesión de DB ---
def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Inicializar BD ---
def init_db():
    Base.metadata.create_all(bind=engine)
