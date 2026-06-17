@echo off

start cmd /k "cd backend && venv\Scripts\activate && uvicorn src.main:app --reload --port 8080"

start cmd /k "cd frontend && venv\Scripts\activate && uvicorn src.app:app --reload --port 8000"

timeout /t 3 > nul

echo Abrindo navegador...
start http://127.0.0.1:8000/cod-externo