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

        except Exception as err:
            print(f"ERRO INESPERADO >> {err}")

    def read_all(self, name_entity: Optional[str] = None) -> list[ModEnsinoOutput]:
        try:
            mod_ensino_all = self.repository.find_all(name_entity)
            response = [self.service.to_dtoOutput(x) for x in mod_ensino_all]
            return response
        except Exception as err:
            print(f"ERRO INESPERADO >> {err}")

    def update(self, id: int, input: ModEnsinoInput) -> ModEnsinoOutput:
        try:
            mod_ensino_all = self.service.to_entity(input)
            response = self.repository.edit(id, mod_ensino_all)
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
            # print(df.to_markdown(index=False))
            df.to_csv(
                "output/teaching-modality.unig_producao.csv",
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
