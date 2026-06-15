# uvicorn src.main:app --reload --port 8080
from fastapi import FastAPI
from src.routers.alt_codigo_externo import router as alt_codigos_externos_router
from src.routers.mod_ensino import router as mod_ensino_router

app = FastAPI()

# /alt-codigos-externos
app.include_router(alt_codigos_externos_router)
# /mods-ensino
app.include_router(mod_ensino_router)
