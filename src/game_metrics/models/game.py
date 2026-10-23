"""
Game ORM model module.
Defines the database schema for video games catalog.
"""

from datetime import date
from sqlalchemy import String, Text, Date
from sqlalchemy.orm import Mapped, mapped_column

from src.game_metrics.core.database import Base


class GameModel(Base):
    """
    Represents a video game entity in the catalog.
    Contains metadata such as title, description, release date, and creators.
    """
    __tablename__ = 'game'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(150), unique=True, nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    release_date: Mapped[date | None] = mapped_column(Date, nullable=True)
    developer: Mapped[str | None] = mapped_column(String(100), nullable=True)
    publisher: Mapped[str | None] = mapped_column(String(100), nullable=True)