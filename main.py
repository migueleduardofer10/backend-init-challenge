from fastapi import FastAPI
from app.users.infrastructure.api import router as user_router
from app.users.infrastructure.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_router)
