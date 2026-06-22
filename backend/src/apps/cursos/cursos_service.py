from io import StringIO

from src.err.exceptios import EntityNotFoundException

from src.apps.cursos.cursos_model import CursosModel
from src.apps.cursos.cursos_dto import CursosInput, CursosOutput

from typing import Any
import pandas as pd


class CursosService:
    def to_entity(self, dto: CursosInput) -> CursosModel:
        return CursosModel(
            name=dto.name,
            externalId=dto.externalId,
            isActive=dto.isActive,
            externalTeachingModalityId=dto.externalTeachingModalityId,
            externalEducationLevelId=dto.externalEducationLevelId,
            courseTypeId=dto.courseTypeId,
        )

    def to_dtoOutput(self, entity: CursosModel):
        print(entity.nivel_ensino)
        if entity.nivel_ensino and entity.modalidade_ensino:
            return CursosOutput(
                id=entity.id,
                name=entity.name,
                externalId=entity.externalId,
                isActive=entity.isActive,
                externalTeachingModalityId=entity.externalTeachingModalityId,
                externalEducationLevelId=entity.externalEducationLevelId,
                courseTypeId=entity.courseTypeId,
                modalidade_ensino={
                    "id": entity.modalidade_ensino.id,
                    "status": entity.modalidade_ensino.status,
                    "name": entity.modalidade_ensino.name,
                    "externalId": entity.modalidade_ensino.externalId,
                    "teachingModalityTypeId": entity.modalidade_ensino.teachingModalityTypeId,
                },
                nivel_ensino={
                    "id": entity.nivel_ensino.id,
                    "status": entity.nivel_ensino.status,
                    "name": entity.nivel_ensino.name,
                    "externalId": entity.nivel_ensino.externalId,
                    "educationLevelTypeId": entity.nivel_ensino.educationLevelTypeId,
                },
            )
        return CursosOutput(
            id=entity.id,
            name=entity.name,
            externalId=entity.externalId,
            isActive=entity.isActive,
            externalTeachingModalityId=entity.externalTeachingModalityId,
            externalEducationLevelId=entity.externalEducationLevelId,
            courseTypeId=entity.courseTypeId,
        )

    def to_dict(self, entity_model: CursosModel) -> dict[str, Any]:
        return {
            "id": entity_model.id,
            "name": entity_model.name,
            "externalId": entity_model.externalId,
            "isActive": entity_model.isActive,
            "externalTeachingModalityId": entity_model.externalTeachingModalityId,
            "externalEducationLevelId": entity_model.externalEducationLevelId,
            "courseTypeId": entity_model.courseTypeId,
        }

    def output_csv(self, all_entity: list[CursosModel]):
        if len(all_entity) <= 0:
            raise EntityNotFoundException()

        output = StringIO()

        entity_dict = [self.to_dict(x) for x in all_entity]
        df = pd.DataFrame(entity_dict)

        df = df.drop(columns=["id"])
        print(df.to_markdown(index=False))
        # df.to_csv(
        #     output,
        #     index=False,
        #     sep=";",
        #     encoding="utf-8",
        # )
        # output.seek(0)

        return output
