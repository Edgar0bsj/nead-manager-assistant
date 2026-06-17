# uvicorn main:app --reload
# uvicorn src.app:app --reload --port 8000

from src.config import app

from src.routers.cod_externo_router import router as ac_externo_router

app.include_router(ac_externo_router)
