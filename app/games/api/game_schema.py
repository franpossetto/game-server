from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from app.games.domain.game_enums import GameType, GameStatus

class GameBase(BaseModel):
    title: str
    description: Optional[str] = None
    key: str
    type: GameType
    icon_url: Optional[str] = None
    status: GameStatus = GameStatus.ACTIVE

class GameCreate(GameBase):
    pass

class GameUpdate(GameBase):
    title: Optional[str] = None
    key: Optional[str] = None
    type: Optional[GameType] = None
    status: Optional[GameStatus] = None

class GameResponse(GameBase):
    id: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
