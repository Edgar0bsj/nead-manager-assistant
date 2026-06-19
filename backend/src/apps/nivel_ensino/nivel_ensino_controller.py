from fastapi.responses import StreamingResponse
from sqlalchemy.exc import IntegrityError
from typing import Optional

from src.err.exceptios import EntityNotFoundException
from fastapi import HTTPException
from src.apps.nivel_ensino.nivel_ensino_repository import NivelEnsinoRepository
from src.apps.nivel_ensino.nivel_ensino_service import NivelEnsinoService
from src.apps.nivel_ensino.nivel_ensino_dto import NivelEnsinoInput, NivelEnsinoOutput
import pandas as pd


class NivelEnsinoController:
    def __init__(self):
        self.service = NivelEnsinoService()
        self.repository = NivelEnsinoRepository()

    def create(self, input: NivelEnsinoInput) -> NivelEnsinoOutput:

        try:
            mod_ensino = self.service.to_entity(input)
            response = self.repository.save(mod_ensino)
            response = self.service.to_dtoOutput(response)
            return response

        except IntegrityError as err:
            raise HTTPException(status_code=409, detail=str(err))
        except Exception as err:
            print(type(err))
            print(f"ERRO INESPERADO >> {err}")

    def read_all(self) -> list[NivelEnsinoOutput]:
        try:
            mod_ensino_all = self.repository.find_all()
            response = [self.service.to_dtoOutput(x) for x in mod_ensino_all]
            return response
        except Exception as err:
            print(type(err))
            print(f"ERRO INESPERADO >> {err}")

    def update(self, id: int, input: NivelEnsinoInput) -> NivelEnsinoOutput:
        try:
            mod_ensino_all = self.service.to_entity(input)
            response = self.repository.edit(id, mod_ensino_all)
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

    def export_csv(self, filter_status: bool):
        try:
            all_mod_ensino = self.repository.find_all(filter_status)
            result_output = self.service.output_csv(all_mod_ensino)

            return StreamingResponse(
                result_output,
                media_type="text/csv",
                headers={
                    "Content-Disposition": "attachment; filename=education-level.unig_producao.csv"
                },
            )
        except Exception as err:
            print(err)
