# uvicorn src.main:app --reload --port 8080
from fastapi import FastAPI
from src.routers.polos import router as polos_router
from src.routers.mod_ensino import router as mod_ensino_router
from src.routers.nivel_ensino import router as nivel_ensino_router
from src.routers.cursos import router as cursos_router

app = FastAPI()

app.include_router(polos_router)
app.include_router(mod_ensino_router)
app.include_router(nivel_ensino_router)
app.include_router(cursos_router)
