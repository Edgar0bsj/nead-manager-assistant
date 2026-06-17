from typing import Optional

from fastapi.responses import StreamingResponse

from src.err.exceptios import EntityNotFoundException
from fastapi import HTTPException
from src.apps.alt_codigo_externo.alt_codigo_externo_repository import (
    AlteracaoCodigoExternoRepository,
)
from src.apps.alt_codigo_externo.alt_codigo_externo_service import (
    AlteracaoCodigoExternoService,
)
from src.apps.alt_codigo_externo.alt_codigo_externo_dto import (
    AlteracaoCodigoExternoInput,
    AlteracaoCodigoExternoOutput,
)
import pandas as pd


class AlteracaoCodigoExternoController:
    def __init__(self):
        self.service = AlteracaoCodigoExternoService()
        self.repository = AlteracaoCodigoExternoRepository()

    def create(self, input: AlteracaoCodigoExternoInput) -> None:

        try:
            al_Codig_Externo = self.service.to_entity(input)
            response = self.repository.save(al_Codig_Externo)
            response = self.service.to_dtoOutput(response)
            return response

        except Exception as err:
            print(f"ERRO INESPERADO >> {err}")

    def read_all(
        self,
        entity_filter: Optional[str] = None,
        status_filter: Optional[bool] = None,
        sistema_filter: Optional[str] = None,
        unidade_filter: Optional[str] = None,
    ) -> list[AlteracaoCodigoExternoOutput]:
        try:
            all_entity = self.repository.find_all(
                entity_filter, status_filter, sistema_filter, unidade_filter
            )
            response = [self.service.to_dtoOutput(x) for x in all_entity]
            return response
        except Exception as err:
            print(f"ERRO INESPERADO >> {err}")

    def update(
        self, id: int, input: AlteracaoCodigoExternoInput
    ) -> AlteracaoCodigoExternoOutput:
        try:
            al_Codig_Externo = self.service.to_entity(input)
            response = self.repository.edit(id, al_Codig_Externo)
            response = self.service.to_dtoOutput(response)
            return response

        except Exception as err:
            print(f"ERRO INESPERADO >> {err}")

    def delete(self, id: int) -> None:
        try:
            self.repository.remove(id)
            return None
        except Exception as err:
            print(f"ERRO INESPERADO >> {err}")

    def read_one(self, id: int):
        try:
            entity = self.repository.find(id)
            response = self.service.to_dtoOutput(entity)
            return response
        except EntityNotFoundException as err:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        except Exception as err:
            print(f"ERRO INESPERADO >> {err}")

    def save_to_csv(
        self,
        entity_filter: Optional[str] = None,
        status_filter: Optional[bool] = None,
        sistema_filter: Optional[str] = None,
        unidade_filter: Optional[str] = None,
    ):
        try:
            all_entity = self.repository.find_all(
                entity_filter, status_filter, sistema_filter, unidade_filter
            )
            output_csv = self.service.csv_export(all_entity)

            return StreamingResponse(
                output_csv,
                media_type="text/csv",
                headers={
                    "Content-Disposition": "attachment; filename=external-id-management.unig_producao.csv"
                },
            )

        except EntityNotFoundException as err:
            raise HTTPException(
                status_code=404, detail="Sem entidade ativos para exportação"
            )
        except Exception as err:
            print(f"ERRO INESPERADO >> {err}")
