from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.games.api import games_router

app = FastAPI(
    title="Game Server",
    description="A FastAPI-based game server application",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(games_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Game Server API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"} 