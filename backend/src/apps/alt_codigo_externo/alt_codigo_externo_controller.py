from typing import Optional

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
            return response

        except Exception as err:
            print(f"ERRO INESPERADO >> {err}")

    def read_all(
        self, name_entity: Optional[str] = None
    ) -> list[AlteracaoCodigoExternoOutput]:
        try:
            all_entity = self.repository.find_all(name_entity)
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

    def save_to_csv(self, status_filter=None, sistema_filter=None, unidade_filter=None):
        try:
            entity_ativos = self.repository.find_all_by(
                status_filter, sistema_filter, unidade_filter
            )

            if len(entity_ativos) <= 0:
                raise EntityNotFoundException()

            entity_dict = [self.service.to_dict(x) for x in entity_ativos]
            df = pd.DataFrame(entity_dict)
            df = df.drop(columns=["id", "status", "sistema", "unidade"])
            # print(df.to_markdown(index=False))
            df.to_csv(
                "output/external-id-management.unig_producao.csv",
                index=False,
                sep=";",
                encoding="utf-8",
            )
            return {"msg": "Arquivo salvo com sucesso!"}

        except EntityNotFoundException as err:
            raise HTTPException(
                status_code=404, detail="Sem entidade ativos para exportação"
            )
        except Exception as err:
            print(f"ERRO INESPERADO >> {err}")
