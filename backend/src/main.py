# uvicorn src.main:app --reload --port 8080
from fastapi import FastAPI
from src.routers.alt_codigo_externo import router

app = FastAPI()

# /alt-codigos-externos
app.include_router(router)
