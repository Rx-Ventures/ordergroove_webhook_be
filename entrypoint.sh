#!/bin/bash


cat << "EOF"
 ________________________
|.----------------------.|
||                      ||
||                      ||
||     .-"````"-.       ||
||    /  _.._    `\     ||
||   / /`    `-.   ; . .||
||   | |__  __  \   |   ||
||.-.| | e`/e`  |   |   ||
||   | |  |     |   |'--||
||   | |  '-    |   |   ||
||   |  \ --'  /|   |   ||
||   |   `;---'\|   |   ||
||   |    |     |   |   ||
||   |  .-'     |   |   ||
||'--|/`        |   |--.||
||   ;    .     ;  _.\  ||
||    `-.;_    /.-'     ||
||         ````         ||
||jgs___________________||
'------------------------'

EOF
if [ "$RUN_MIGRATIONS" = "true" ]; then
    echo "Running database migrations..."
    alembic upgrade head
    echo "Migrations complete."
fi

echo "Starting FastAPI server..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8001

