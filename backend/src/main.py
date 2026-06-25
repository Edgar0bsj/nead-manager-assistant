# uvicorn src.main:app --reload --port 8080

# Dependency
from fastapi import FastAPI

# Routes
from src.routers import polos_router
from src.routers import mod_ensino_router
from src.routers import nivel_ensino_router
from src.routers import cursos_router

# Exceptions
from src.exceptions import erros_handler

app = FastAPI()
erros_handler(app)

app.include_router(polos_router)
app.include_router(mod_ensino_router)
app.include_router(nivel_ensino_router)
app.include_router(cursos_router)
