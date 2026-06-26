# Dependency
from fastapi.responses import StreamingResponse
from fastapi import HTTPException, UploadFile

# Packages
from .cursos_repository import CursosRepository
from .cursos_service import CursosService
from .cursos_dto import CursosInput, CursosOutput

# Exceptions
from sqlalchemy.exc import IntegrityError


class CursosController:
    def __init__(self):
        self.service = CursosService()
        self.repository = CursosRepository()

    def create(self, input: CursosInput) -> CursosOutput:

        curso = self.service.to_entity(input)
        response = self.repository.save(curso)
        response = self.service.to_dtoOutput(response)
        return response

    def read_all(self) -> list[CursosOutput]:

        cursos_all = self.repository.find_all()
        response = [self.service.to_dtoOutput(x) for x in cursos_all]
        return response

    def update(self, id: int, input: CursosInput) -> CursosOutput:

        cursos_all = self.service.to_entity(input)
        response = self.repository.edit(id, cursos_all)
        response = self.service.to_dtoOutput(response)
        return response

    def delete(self, id: int) -> None:

        self.repository.remove(id)
        return None

    def read_one(self, id: int):

        entity = self.repository.find(id)
        response = self.service.to_dtoOutput(entity)
        return response

    def export_csv(self):

        all_cursos = self.repository.find_all()
        result_output = self.service.output_csv(all_cursos)

        return StreamingResponse(
            result_output,
            media_type="text/csv",
            headers={
                "Content-Disposition": "attachment; filename=course.unig_producao.csv"
            },
        )

    async def process_file_xlsx(self, file: UploadFile):
        df = await self.service.xlsx_to_dataframe(file)
        df = await self.service.df_remover_cursos_duplicados(df)

        df = self.service.prepare_dataframe(df)

        data_dict = df.to_dict(orient="records")

        found, not_found = await self.service.verify_persistence(data_dict, self)

        created, erros_created = await self.service.persist(not_found, self)

        updated, erros_updated = await self.service.persist(found, self, update=True)

        outputResponse = {}
        outputResponse["created"] = created
        outputResponse["erros_created"] = erros_created
        outputResponse["updated"] = updated
        outputResponse["erros_updated"] = erros_updated

        return outputResponse
