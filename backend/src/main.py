# uvicorn src.main:app --reload --port 8080
from fastapi import FastAPI
from src.routers.alt_codigo_externo import router as alt_codigos_externos_router
from src.routers.mod_ensino import router as mod_ensino_router
from src.routers.nivel_ensino import router as nivel_ensino_router
from src.routers.cursos import router as cursos_router

app = FastAPI()

app.include_router(alt_codigos_externos_router)
app.include_router(mod_ensino_router)
app.include_router(nivel_ensino_router)
app.include_router(cursos_router)
