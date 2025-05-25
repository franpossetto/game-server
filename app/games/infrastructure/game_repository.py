from sqlalchemy.orm import Session

from app.games.infrastructure.game_model import GameModel

class GameRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(GameModel).all()

    def get_by_id(self, game_id: str):
        return self.db.query(GameModel).filter(GameModel.id == game_id).first()

    def get_by_key(self, key: str):
        return self.db.query(GameModel).filter(GameModel.key == key).first()

    def create(self, game: GameModel):
        self.db.add(game)
        self.db.commit()
        self.db.refresh(game)
        return game

    def update(self, game: GameModel):
        self.db.commit()
        self.db.refresh(game)
        return game

    def delete(self, game_id: str):
        game = self.get_by_id(game_id)
        if game:
            self.db.delete(game)
            self.db.commit()
        return game 