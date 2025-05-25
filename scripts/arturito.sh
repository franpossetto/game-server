#!/bin/bash

# Colors for messages
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# Function to display messages
print_message() {
    echo -e "${GREEN}[Arturito]${NC} $1"
}

# Cleanup function when exiting
cleanup() {
    print_message "Stopping containers..."
    docker-compose down
    print_message "Goodbye! 👋"
    exit 0
}

# Capture Ctrl+C
trap cleanup SIGINT

# Start containers
print_message "Starting containers..."
docker-compose up -d

# Start the application
print_message "Starting the application..."
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# If we reach here, it means the application stopped
cleanup
