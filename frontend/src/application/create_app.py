from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.presentation.polo import polo_router
from src.presentation.modalidade_ensino import modEns_router
from src.presentation.nivel_ensino import nivelEns_router
from src.presentation.cursos import curso_router


def create_app() -> FastAPI:
    _app = None

    _app = initialize_app(_app)
    _app = config_statics_fille(_app)
    _app = config_routers(_app)

    return _app


def initialize_app(app) -> FastAPI:
    app = FastAPI()
    return app


def config_statics_fille(app: FastAPI) -> FastAPI:

    app.mount("/assets", StaticFiles(directory="src/view/assets"), name="assets")

    return app


def config_routers(app: FastAPI) -> FastAPI:

    app.include_router(polo_router)
    app.include_router(modEns_router)
    app.include_router(nivelEns_router)
    app.include_router(curso_router)

    return app
