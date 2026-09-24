from sqlalchemy import String, Column, DateTime, ForeignKey
from datetime import datetime

from app.database import Base


class Blog(Base):

    __tablename__ = "blogs"

    # Primary key
    id = Column(String(36), primary_key=True)

    # Blog title
    title = Column(String(200), nullable=False)

    # Blog content
    content = Column(String, nullable=False)

    # Foreign key referencing users.id
    user_id = Column(String(36), ForeignKey("users.id"), nullable=False)

    # Blog creation time
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Blog update time
    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )