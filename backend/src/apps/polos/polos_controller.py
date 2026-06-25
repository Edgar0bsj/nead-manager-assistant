# Packages
from .polos_repository import PoloRepository
from .polos_service import PoloService
from .polos_dto import PoloInput, PoloOutput

# Exceptions
from src.exceptions import EntityNotFoundException


class PoloController:
    def __init__(self):
        self.service = PoloService()
        self.repository = PoloRepository()

    def create(self, input: PoloInput) -> PoloOutput:

        polo = self.service.to_entity(input)
        response = self.repository.save(polo)
        response = self.service.to_dtoOutput(response)
        return response

    def read_all(self) -> list[PoloOutput]:

        all_entity = self.repository.find_all()
        response = [self.service.to_dtoOutput(x) for x in all_entity]
        return response

    def update(self, id: int, input: PoloInput) -> PoloOutput:

        all_polos = self.service.to_entity(input)
        response = self.repository.edit(id, all_polos)
        response = self.service.to_dtoOutput(response)
        return response

    def delete(self, id: int) -> None:

        self.repository.remove(id)
        return None

    def read_one(self, id: int) -> PoloOutput | None:

        entity = self.repository.find(id)

        if entity is None:
            raise EntityNotFoundException("Polo não encontrado")

        response = self.service.to_dtoOutput(entity)
        return response
