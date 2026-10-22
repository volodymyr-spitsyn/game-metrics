"""
Database core module.
Configures the SQLAlchemy 2.0 async engine, session factory, and DeclarativeBase.
"""

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from app.core.config import get_settings

# Retrieve settings via a singleton
settings = get_settings()

# Creating a unified asynchronous database engine
engine = create_async_engine(settings.DATABASE_URL, echo=True)

# Create a session factory (defaults to AsyncSession)
SessionMaker = async_sessionmaker(engine, expire_on_commit=False)


# Base class for future ORM models (tables)
class Base(DeclarativeBase):
    pass