from datetime import datetime
from .game_enums import GameType, GameStatus

class Game:
    def __init__(
        self,
        id: str,
        title: str,
        description: str | None,
        key: str,
        type: GameType,
        icon_url: str | None,
        status: GameStatus = GameStatus.ACTIVE,
        created_at: datetime | None = None,
        updated_at: datetime | None = None
    ):
        self.id = id
        self.title = title
        self.description = description
        self.key = key
        self.type = type
        self.icon_url = icon_url
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at 