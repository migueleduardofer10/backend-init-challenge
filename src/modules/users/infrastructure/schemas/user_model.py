# --- Modelo SQLAlchemy para tabla users ---
from sqlalchemy import Column, Integer, String
from core.db import Base 

class UserModel(Base):
    __tablename__ = "users"

    id  = Column(Integer, primary_key=True, index=True)
    vc_name = Column(String, nullable=False)
    vc_email = Column(String, unique=True, index=True, nullable=False)
    vc_password = Column(String, nullable=False)
