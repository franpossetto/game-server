from enum import Enum

class GameType(str, Enum):
    SINGLE_MODE = "single_mode"
    MULTI_MODE = "multi_mode"

class GameStatus(str, Enum):
    ACTIVE = "active"
    INACTIVE = "inactive"
    MAINTENANCE = "maintenance" 