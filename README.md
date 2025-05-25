# Game Server API

## Getting Started

1. Clone the repository
```bash
git clone [repository-url]
cd game-server
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Start the database with Docker
```bash
docker-compose up -d
```

4. Start the server
```bash
uvicorn app.main:app --reload
```

Alternatively, you can use the arturito script which handles both database and server:
```bash
./scripts/arturito.sh
```

## Project Structure
```
game-server/
├── app/                    # Application module
│   ├── core/               # Core configuration
│   │   └── database.py     # Database setup
│   ├── games/              # Games module
│   │   ├── api/            # API endpoints and schemas
│   │   ├── application/    # Business logic and services
│   │   ├── domain/         # Business models and rules
│   │   └── infrastructure/ # Database models and repositories
│   └── main.py             # Application entry point
├── alembic/                # Database migrations
├── scripts/                # Utility scripts
│   └── arturito.sh         # Development startup script
├── docker-compose.yml      # Docker services configuration
└── requirements.txt        # Python dependencies
```

## API Documentation
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## License
MIT License