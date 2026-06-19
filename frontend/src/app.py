# uvicorn src.app:app --reload --port 8000

from src.config import app

from src.routers.cod_externo_router import router as ac_externo_router
from src.routers.mod_ensino_router import router as mod_ensino_router
from src.routers.nivel_ensino_router import router as nivel_ensino_router

app.include_router(ac_externo_router)
app.include_router(mod_ensino_router)
app.include_router(nivel_ensino_router)
