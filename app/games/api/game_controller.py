from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.games.api.game_schema import GameCreate, GameResponse, GameUpdate
from app.games.application.game_service import GameService
from typing import List

router = APIRouter(prefix="/games", tags=["games"])

def get_game_service(db: Session = Depends(get_db)) -> GameService:
    return GameService(db)

@router.get("/", response_model=List[GameResponse])
def get_games(service: GameService = Depends(get_game_service)):
    return service.get_all_games()

@router.get("/{game_id}", response_model=GameResponse)
def get_game(game_id: str, service: GameService = Depends(get_game_service)):
    game = service.get_game_by_id(game_id)
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    return game

@router.post("/", response_model=GameResponse)
def create_game(game: GameCreate, service: GameService = Depends(get_game_service)):
    return service.create_game(game.model_dump())

@router.put("/{game_id}", response_model=GameResponse)
def update_game(game_id: str, game: GameUpdate, service: GameService = Depends(get_game_service)):
    updated_game = service.update_game(game_id, game.model_dump(exclude_unset=True))
    if not updated_game:
        raise HTTPException(status_code=404, detail="Game not found")
    return updated_game

@router.delete("/{game_id}")
def delete_game(game_id: str, service: GameService = Depends(get_game_service)):
    game = service.delete_game(game_id)
    if not game:
        raise HTTPException(status_code=404, detail="Game not found")
    return {"message": "Game deleted successfully"} 