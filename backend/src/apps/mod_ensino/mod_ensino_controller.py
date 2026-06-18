from fastapi.responses import StreamingResponse
from sqlalchemy.exc import IntegrityError
from typing import Optional

from src.err.exceptios import EntityNotFoundException
from fastapi import HTTPException
from src.apps.mod_ensino.mod_ensino_repository import ModEnsinoRepository
from src.apps.mod_ensino.mod_ensino_service import ModEnsinoService
from src.apps.mod_ensino.mod_ensino_dto import ModEnsinoInput, ModEnsinoOutput
import pandas as pd


class ModEnsinoController:
    def __init__(self):
        self.service = ModEnsinoService()
        self.repository = ModEnsinoRepository()

    def create(self, input: ModEnsinoInput) -> ModEnsinoOutput:

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

    def read_all(self) -> list[ModEnsinoOutput]:
        try:
            mod_ensino_all = self.repository.find_all()
            response = [self.service.to_dtoOutput(x) for x in mod_ensino_all]
            return response
        except Exception as err:
            print(type(err))
            print(f"ERRO INESPERADO >> {err}")

    def update(self, id: int, input: ModEnsinoInput) -> ModEnsinoOutput:
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
                    "Content-Disposition": "attachment; filename=teaching-modality.unig_producao.csv"
                },
            )
        except Exception as err:
            print(err)
