# uvicorn src.app:app --reload --port 8000

from src.config import app

from src.routers.polos_router import router as polos_router
from src.routers.mod_ensino_router import router as mod_ensino_router
from src.routers.nivel_ensino_router import router as nivel_ensino_router
from src.routers.cursos_router import router as cursos_router

app.include_router(polos_router)
app.include_router(mod_ensino_router)
app.include_router(nivel_ensino_router)
app.include_router(cursos_router)
