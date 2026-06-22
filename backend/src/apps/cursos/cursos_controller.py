from fastapi.responses import StreamingResponse
from sqlalchemy.exc import IntegrityError
from typing import Optional

from src.err.exceptios import EntityNotFoundException
from fastapi import HTTPException
from src.apps.cursos.cursos_repository import CursosRepository
from src.apps.cursos.cursos_service import CursosService
from src.apps.cursos.cursos_dto import CursosInput, CursosOutput
import pandas as pd


class CursosController:
    def __init__(self):
        self.service = CursosService()
        self.repository = CursosRepository()

    def create(self, input: CursosInput) -> CursosOutput:

        try:
            curso = self.service.to_entity(input)
            response = self.repository.save(curso)
            response = self.service.to_dtoOutput(response)
            return response

        except IntegrityError as err:
            raise HTTPException(status_code=409, detail=str(err))
        except Exception as err:
            print(type(err))
            print(f"ERRO INESPERADO >> {err}")

    def read_all(self) -> list[CursosOutput]:
        try:
            cursos_all = self.repository.find_all()
            response = [self.service.to_dtoOutput(x) for x in cursos_all]
            return response
        except Exception as err:
            print(type(err))
            print(f"ERRO INESPERADO >> {err}")

    def update(self, id: int, input: CursosInput) -> CursosOutput:
        try:
            cursos_all = self.service.to_entity(input)
            response = self.repository.edit(id, cursos_all)
            response = self.service.to_dtoOutput(response)
            return response

        except IntegrityError as err:
            raise HTTPException(status_code=409, detail=str(err))
        except Exception as err:
            print(type(err))
            print(f"ERRO INESPERADO >> {err}")

    def delete(self, id: int) -> None:
        try:
            self.repository.remove(id)
            return None
        except Exception as err:
            print(type(err))
            print(f"ERRO INESPERADO >> {err}")

    def read_one(self, id: int):
        try:
            entity = self.repository.find(id)
            response = self.service.to_dtoOutput(entity)
            return response
        except EntityNotFoundException as err:
            raise HTTPException(status_code=404, detail="id não encontrado")
        except Exception as err:
            print(type(err))
            print(f"ERRO INESPERADO >> {err}")

    def export_csv(self):
        try:
            all_cursos = self.repository.find_all()
            result_output = self.service.output_csv(all_cursos)

            # return {"msg": ";D"}
            return StreamingResponse(
                result_output,
                media_type="text/csv",
                headers={
                    "Content-Disposition": "attachment; filename=course.unig_producao.csv"
                },
            )
        except Exception as err:
            print(err)
