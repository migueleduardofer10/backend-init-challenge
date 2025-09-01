# app/core/providers.py
from typing import Generator
from fastapi import Depends
from sqlalchemy.orm import Session

from core.config import settings
from core.db import get_session

from modules.users.infrastructure.rabbitmq_publisher import RabbitMQPublisher
from modules.users.infrastructure.repositories.user_repo_sqlalchemy import SqlAlchemyUserRepository
from modules.users.application.commands import CreateUserHandler, PersistUserHandler
from modules.users.application.queries import GetUserByIdHandler

def get_settings():
    return settings

def get_publisher(cfg = Depends(get_settings)) -> RabbitMQPublisher:
    return RabbitMQPublisher(
        url=cfg.RABBITMQ_URL,
        queue=cfg.RABBITMQ_QUEUE
    )

def get_user_repository(session: Session = Depends(get_session)) -> SqlAlchemyUserRepository:
    return SqlAlchemyUserRepository(session)

def get_create_user_handler(
    publisher: RabbitMQPublisher = Depends(get_publisher),
) -> CreateUserHandler:
    return CreateUserHandler(publisher=publisher)

def get_persist_user_handler(
    repo: SqlAlchemyUserRepository = Depends(get_user_repository),
) -> PersistUserHandler:
    return PersistUserHandler(repo=repo)

def get_user_by_id_handler(
    repo: SqlAlchemyUserRepository = Depends(get_user_repository),
) -> GetUserByIdHandler:
    return GetUserByIdHandler(repo)
