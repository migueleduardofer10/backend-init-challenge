from dependency_injector import containers, providers
from core.config import settings
from core.db import SessionLocal

from modules.users.infrastructure.rabbitmq_publisher import RabbitMQPublisher
from modules.users.infrastructure.repositories.user_repo_sqlalchemy import SqlAlchemyUserRepository

from modules.users.application.commands import PublishUserHandler, PersistUserHandler
from modules.users.application.queries import GetUserByIdQuery, GetUserByIdHandler
from modules.users.domain.policies import PasswordPolicy

def _session_resource():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "modules.users.infrastructure.rabbitmq_consumer",
        ]
    )

    # --- Config ---
    config = providers.Object(settings)

    # --- Recursos base / Infra ---
    db_session = providers.Resource(_session_resource)

    publisher = providers.Factory(
        RabbitMQPublisher,
        url=config.provided.RABBITMQ_URL,
        queue=config.provided.RABBITMQ_QUEUE,
    )

    user_repository = providers.Factory(
        SqlAlchemyUserRepository,
        session=db_session,
    )

    password_policy = providers.Factory(PasswordPolicy)

    # --- Handlers ---
    publish_user_handler = providers.Factory(
        PublishUserHandler,
        publisher=publisher,
    )

    get_user_by_id_handler = providers.Factory(
        GetUserByIdHandler,
        repo=user_repository,
    )

    persist_user_handler = providers.Factory(
        PersistUserHandler,
        repo=user_repository,
        password_policy=password_policy,
    )
