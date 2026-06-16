from typing import Optional

from src.err.exceptios import EntityNotFoundException
from fastapi import HTTPException
from src.apps.cursos.cursos_repository import CursoRepository
from src.apps.cursos.cursos_service import CursoService
from src.apps.cursos.cursos_dto import CursoInput, CursoOutput
import pandas as pd


class CursoController:
    def __init__(self):
        self.service = CursoService()
        self.repository = CursoRepository()

    def create(self, input: CursoInput) -> CursoOutput:

        try:
            curso = self.service.to_entity(input)
            response = self.repository.save(curso)
            response = self.service.to_dtoOutput(response)
            return response

        except Exception as err:
            print(f"ERRO INESPERADO >> {err}")

    def read_all(self, name_entity: Optional[str] = None) -> list[CursoOutput]:
        try:
            curso = self.repository.find_all(name_entity)
            response = [self.service.to_dtoOutput(x) for x in curso]
            return response
        except Exception as err:
            print(f"ERRO INESPERADO >> {err}")

    def update(self, id: int, input: CursoInput) -> CursoOutput:
        try:
            cursos_all = self.service.to_entity(input)
            response = self.repository.edit(id, cursos_all)
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
            cursos = self.repository.find_all_by(
                status_filter, sistema_filter, unidade_filter
            )

            if len(cursos) <= 0:
                raise EntityNotFoundException()

            entity_dict = [self.service.to_dict(x) for x in cursos]
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
