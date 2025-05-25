from sqlalchemy import Boolean, Column, String, DateTime
from sqlalchemy.sql import func
from app.core.database import Base
from app.games.domain.game_enums import GameType, GameStatus

class GameModel(Base):
    __tablename__ = "games"

    id = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    key = Column(String, nullable=False, unique=True)
    type = Column(String, nullable=False)
    icon_url = Column(String, nullable=True)
    status = Column(Boolean, nullable=False, default=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now()) 