from sqlalchemy import Column, Integer, String
from app.core.db import Base  # ajusta import si tu Base está en otro path

class UserModel(Base):
    __tablename__ = "users"

    i_user_id = Column(Integer, primary_key=True, index=True)
    vc_name = Column(String, nullable=False)
    vc_email = Column(String, unique=True, index=True, nullable=False)
    vc_password = Column(String, nullable=False)
