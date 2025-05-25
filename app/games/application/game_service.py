from sqlalchemy.orm import Session
from app.games.domain import Game, GameType, GameStatus
from app.games.infrastructure.game_repository import GameRepository
from app.games.infrastructure.game_model import GameModel
import uuid

class GameService:
    def __init__(self, db: Session):
        self.repository = GameRepository(db)

    def get_all_games(self):
        games = self.repository.get_all()
        return [self._to_domain(game) for game in games]

    def get_game_by_id(self, game_id: str):
        game = self.repository.get_by_id(game_id)
        return self._to_domain(game) if game else None

    def get_game_by_key(self, key: str):
        game = self.repository.get_by_key(key)
        return self._to_domain(game) if game else None

    def create_game(self, game_data: dict):
        game = Game(
            id=str(uuid.uuid4()),
            title=game_data['title'],
            description=game_data.get('description'),
            key=game_data['key'],
            type=GameType(game_data['type']),
            icon_url=game_data.get('icon_url'),
            status=GameStatus.ACTIVE if game_data.get('status', True) else GameStatus.INACTIVE
        )
        
        game_model = GameModel(
            id=game.id,
            title=game.title,
            description=game.description,
            key=game.key,
            type=game.type,
            icon_url=game.icon_url,
            status=game.status == GameStatus.ACTIVE
        )
        
        created_game = self.repository.create(game_model)
        return self._to_domain(created_game)

    def update_game(self, game_id: str, game_data: dict):
        existing_game = self.repository.get_by_id(game_id)
        if not existing_game:
            return None
        
        game = Game(
            id=game_id,
            title=game_data.get('title', existing_game.title),
            description=game_data.get('description', existing_game.description),
            key=game_data.get('key', existing_game.key),
            type=GameType(game_data.get('type', existing_game.type)),
            icon_url=game_data.get('icon_url', existing_game.icon_url),
            status=GameStatus.ACTIVE if game_data.get('status', True) else GameStatus.INACTIVE
        )
        
        for key, value in self._to_infrastructure(game).items():
            setattr(existing_game, key, value)
        
        updated_game = self.repository.update(existing_game)
        return self._to_domain(updated_game)

    def delete_game(self, game_id: str):
        game = self.repository.delete(game_id)
        return self._to_domain(game) if game else None

    def _to_domain(self, game_model):
        if not game_model:
            return None
        return Game(
            id=game_model.id,
            title=game_model.title,
            description=game_model.description,
            key=game_model.key,
            type=game_model.type,
            icon_url=game_model.icon_url,
            status=GameStatus.ACTIVE if game_model.status else GameStatus.INACTIVE,
            created_at=game_model.created_at,
            updated_at=game_model.updated_at
        )

    def _to_infrastructure(self, game: Game):
        return {
            'id': game.id,
            'title': game.title,
            'description': game.description,
            'key': game.key,
            'type': game.type,
            'icon_url': game.icon_url,
            'status': game.status == GameStatus.ACTIVE,
            'created_at': game.created_at,
            'updated_at': game.updated_at
        } 