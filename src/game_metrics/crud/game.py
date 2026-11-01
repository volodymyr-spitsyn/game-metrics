"""
CRUD operations for Game model.
"""

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from game_metrics.models.game import GameModel
from schemas.game import GameCreate


async def get_games(db: AsyncSession) -> list[GameModel]:
    """Retrieve all games from the database."""
    result = await db.execute(select(GameModel))
    return list(result.scalars().all())

async def create_game(db: AsyncSession, game: GameCreate) -> GameModel:
    """Create a new game in the database."""
