# Dependency
from fastapi import HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.exc import IntegrityError

# Packages
from .mod_ensino_repository import ModEnsinoRepository
from .mod_ensino_service import ModEnsinoService
from .mod_ensino_dto import ModEnsinoInput, ModEnsinoOutput


class ModEnsinoController:
    def __init__(self):
        self.service = ModEnsinoService()
        self.repository = ModEnsinoRepository()

    def create(self, input: ModEnsinoInput) -> ModEnsinoOutput:

        mod_ensino = self.service.to_entity(input)
        response = self.repository.save(mod_ensino)
        response = self.service.to_dtoOutput(response)
        return response

    def read_all(self) -> list[ModEnsinoOutput]:

        mod_ensino_all = self.repository.find_all()
        response = [self.service.to_dtoOutput(x) for x in mod_ensino_all]
        return response

    def update(self, id: int, input: ModEnsinoInput) -> ModEnsinoOutput:

        mod_ensino_all = self.service.to_entity(input)
        response = self.repository.edit(id, mod_ensino_all)
        response = self.service.to_dtoOutput(response)
        return response

    def delete(self, id: int) -> None:

        self.repository.remove(id)
        return None

    def read_one(self, id: int):

        entity = self.repository.find(id)
        response = self.service.to_dtoOutput(entity)
        return response

    def export_csv(self, filter_status: bool):

        all_mod_ensino = self.repository.find_all(filter_status)
        result_output = self.service.output_csv(all_mod_ensino)

        return StreamingResponse(
            result_output,
            media_type="text/csv",
            headers={
                "Content-Disposition": "attachment; filename=teaching-modality.unig_producao.csv"
            },
        )
