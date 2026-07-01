# uvicorn src.main:app --reload --port 8080

# Dependency
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Routes
from src.routers import polos_router
from src.routers import mod_ensino_router
from src.routers import nivel_ensino_router
from src.routers import cursos_router

# Exceptions
from src.exceptions import erros_handler

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8000"],  # origem do seu frontend
    allow_credentials=True,
    allow_methods=["*"],  # permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # permite todos os headers
)

erros_handler(app)

app.include_router(polos_router)
app.include_router(mod_ensino_router)
app.include_router(nivel_ensino_router)
app.include_router(cursos_router)
