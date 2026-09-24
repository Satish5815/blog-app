from sqlalchemy import String, Column, DateTime
from datetime import datetime

from app.database import Base


class User(Base):
    __tablename__ = "users"

    # Unique primary key for the user
    id = Column(String(36), primary_key=True)

    # User's name
    name = Column(String(100), nullable=False)

    # User's email
    email = Column(String(150), unique=True, nullable=False)

    # Hashed password, never store plain password
    password_hash = Column(String(255), nullable=False)

    # Account creation time
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)