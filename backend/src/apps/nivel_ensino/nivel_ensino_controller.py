from typing import Optional

from src.err.exceptios import EntityNotFoundException
from fastapi import HTTPException
from src.apps.nivel_ensino.nivel_ensino_repository import NivelEnsinoRepository
from src.apps.nivel_ensino.nivel_ensino_service import NivelEnsinoService
from src.apps.nivel_ensino.nivel_ensino_dto import NivelEnsinoOutput, NivelEnsinoInput
import pandas as pd


class NivelEnsinoController:
    def __init__(self):
        self.service = NivelEnsinoService()
        self.repository = NivelEnsinoRepository()

    def create(self, input: NivelEnsinoInput) -> NivelEnsinoOutput:

        try:
            nivel_ensino = self.service.to_entity(input)
            response = self.repository.save(nivel_ensino)
            response = self.service.to_dtoOutput(response)
            return response

        except Exception as err:
            print(f"ERRO INESPERADO >> {err}")

    def read_all(self, name_entity: Optional[str] = None) -> list[NivelEnsinoOutput]:
        try:
            nivel_ensino_all = self.repository.find_all(name_entity)
            response = [self.service.to_dtoOutput(x) for x in nivel_ensino_all]
            return response
        except Exception as err:
            print(f"ERRO INESPERADO >> {err}")

    def update(self, id: int, input: NivelEnsinoInput) -> NivelEnsinoOutput:
        try:
            nivel_ensino_all = self.service.to_entity(input)
            response = self.repository.edit(id, nivel_ensino_all)
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
            raise HTTPException(status_code=404, detail="id não encontrado")
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
            print(df.to_markdown(index=False))
            # df.to_csv(
            #     "output/education-level.unig_producao.csv",
            #     index=False,
            #     sep=";",
            #     encoding="utf-8",
            # )
            return {"msg": "Arquivo salvo com sucesso!"}

        except EntityNotFoundException as err:
            raise HTTPException(
                status_code=404, detail="Sem entidade ativos para exportação"
            )
        except Exception as err:
            print(f"ERRO INESPERADO >> {err}")
