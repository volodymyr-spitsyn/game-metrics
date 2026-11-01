"""
Pydantic schemas for Game entity validation and serialization.
"""

from datetime import date
from pydantic import BaseModel, ConfigDict


class GameBase(BaseModel):
    title: str
    description: str
    release_date: date

class GameCreate(GameBase):
    """Schema for adding a new game to the catalog."""
    pass

class GameResponse(GameBase):
    """Schema for returning game data to the client, including database ID."""
    id: int

    model_config = ConfigDict(from_attributes=True)