# Dependency
from fastapi import Request
from fastapi.responses import JSONResponse

# Packages
from ..process_error import EntityNotFoundException, UniqueConstraintViolationException


def erros_handler(app):
    # ///////////////////////////////////////////////////////////////
    # ----------------- CONFLICT ------------------------------------
    # ///////////////////////////////////////////////////////////////
    @app.exception_handler(UniqueConstraintViolationException)
    async def DatabaseOperational_handler(
        request: Request, exc: UniqueConstraintViolationException
    ):
        return JSONResponse(
            status_code=409, content={"message": f"Ocorreu um erro: {exc.msg}"}
        )

    # ///////////////////////////////////////////////////////////////
    # ---------------- NOT FOUND ------------------------------------
    # ///////////////////////////////////////////////////////////////
    @app.exception_handler(EntityNotFoundException)
    async def EntityNotFoundException_handler(
        request: Request, exc: EntityNotFoundException
    ):
        return JSONResponse(
            status_code=404, content={"message": f"Ocorreu um erro: {exc.msg}"}
        )
