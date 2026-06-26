# uvicorn src.main:app --reload --port 8000
from src.application import create_app

app = create_app()
