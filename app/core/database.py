# configuring the SQLAlchemy 2.0 engine (create_async_engine), the session factory (async_sessionmaker), and the base class for models (DeclarativeBase).

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from app.core.config import get_settings

# Получаем настройки через синглтон
settings = get_settings()

# Создаем единый асинхронный движок базы данных
engine = create_async_engine(settings.DATABASE_URL, echo=True)

# Создаем фабрику сессий (class_ по умолчанию AsyncSession, указывать DeclarativeBase здесь не нужно!)
SessionMaker = async_sessionmaker(engine, expire_on_commit=False)

# Базовый класс для будущих ORM-моделей (таблиц)
class Base(DeclarativeBase):
    pass

