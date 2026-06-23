from io import StringIO

from src.err.exceptios import EntityNotFoundException
from src.apps.nivel_ensino.nivel_ensino_model import NivelEnsinoModel
from src.apps.nivel_ensino.nivel_ensino_dto import NivelEnsinoInput, NivelEnsinoOutput
from typing import Any
import pandas as pd


class NivelEnsinoService:
    def to_entity(self, dto: NivelEnsinoInput) -> NivelEnsinoModel:
        return NivelEnsinoModel(
            status=dto.status,
            name=dto.name,
            externalId=dto.externalId,
            educationLevelTypeId=dto.educationLevelTypeId,
        )

    def to_dtoOutput(self, entity: NivelEnsinoModel):

        data = {
            "id": entity.id,
            "status": entity.status,
            "name": entity.name,
            "externalId": entity.externalId,
            "educationLevelTypeId": entity.educationLevelTypeId,
        }

        if entity.cursos:
            data["cursos"] = []
            for i in range(len(entity.cursos)):
                data["cursos"].append(
                    {
                        "id": entity.cursos[i].id,
                        "name": entity.cursos[i].name,
                        "externalId": entity.cursos[i].externalId,
                        "isActive": entity.cursos[i].isActive,
                        "externalTeachingModalityId": entity.cursos[
                            i
                        ].externalTeachingModalityId,
                        "externalEducationLevelId": entity.cursos[
                            i
                        ].externalEducationLevelId,
                        "courseTypeId": entity.cursos[i].courseTypeId,
                    }
                )

        return NivelEnsinoOutput(**data)

    def to_dict(self, entity_model: NivelEnsinoModel) -> dict[str, Any]:
        return {
            "id": entity_model.id,
            "status": entity_model.status,
            "name": entity_model.name,
            "externalId": entity_model.externalId,
            "educationLevelTypeId": entity_model.educationLevelTypeId,
        }

    def output_csv(self, all_entity: list[NivelEnsinoModel]):
        if len(all_entity) <= 0:
            raise EntityNotFoundException()

        output = StringIO()

        entity_dict = [self.to_dict(x) for x in all_entity]
        df = pd.DataFrame(entity_dict)

        df = df.drop(columns=["id", "status"])
        # print(df.to_markdown(index=False))
        df.to_csv(
            output,
            index=False,
            sep=";",
            encoding="utf-8",
        )
        output.seek(0)

        return output
