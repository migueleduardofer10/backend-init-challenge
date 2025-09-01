from fastapi import FastAPI, APIRouter

from app.api.users_http import router as users_router
from app.api.auth_http import router as auth_router
from core.config import settings
from core.db import init_db

# ---- Inicializar DB ----
init_db()

## ---- Crear instancia FastAPI ----
app = FastAPI(title="Backend Init")

## ---- Registrar routers ----
api_router = APIRouter(prefix="/api")
api_router.include_router(users_router)
api_router.include_router(auth_router)

app.include_router(api_router)

## ---- Root endpoint ----
@app.get("/")
def root():
    return {
        "app": settings.APP_ENV,
        "status": "running"
    }