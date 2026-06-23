from typing import Optional

from fastapi.responses import StreamingResponse

from src.err.exceptios import EntityNotFoundException
from fastapi import HTTPException
from src.apps.polos.polos_repository import PoloRepository
from src.apps.polos.polos_service import PoloService
from src.apps.polos.polos_dto import PoloInput, PoloOutput


class PoloController:
    def __init__(self):
        self.service = PoloService()
        self.repository = PoloRepository()

    def create(self, input: PoloInput) -> PoloOutput:

        try:
            polo = self.service.to_entity(input)
            response = self.repository.save(polo)
            response = self.service.to_dtoOutput(response)
            return response

        except Exception as err:
            print(f"ERRO INESPERADO >> {err}")

    def read_all(self) -> list[PoloOutput]:
        try:
            all_entity = self.repository.find_all()
            response = [self.service.to_dtoOutput(x) for x in all_entity]
            return response
        except Exception as err:
            print(f"ERRO INESPERADO >> {err}")

    def update(self, id: int, input: PoloInput) -> PoloOutput:
        try:
            all_polos = self.service.to_entity(input)
            response = self.repository.edit(id, all_polos)
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

    def read_one(self, id: int) -> PoloOutput | None:
        try:
            entity = self.repository.find(id)
            response = self.service.to_dtoOutput(entity)
            return response
        except EntityNotFoundException as err:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        except Exception as err:
            print(f"ERRO INESPERADO >> {err}")
