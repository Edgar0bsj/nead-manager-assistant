# Dependency
import pandas as pd
from io import StringIO, BytesIO
from fastapi import UploadFile
from typing import Any

# Packages
from .cursos_model import CursosModel
from .cursos_dto import CursosInput, CursosOutput
from .util.df_format import (
    normalize_text,
    set_courseTypeId,
    set_externalId,
)

# Exceptions
from src.exceptions import EntityNotFoundException


class CursosService:
    def to_entity(self, dto: CursosInput) -> CursosModel:
        return CursosModel(
            name=dto.name,
            externalId=dto.externalId,
            isActive=dto.isActive,
            courseTypeId=dto.courseTypeId,
            externalTeachingModalityId=dto.externalTeachingModalityId,
            externalEducationLevelId=dto.externalEducationLevelId,
            polo_id=dto.polo_id,
        )

    def to_dtoOutput(self, entity: CursosModel):

        data = {
            "id": entity.id,
            "name": entity.name,
            "externalId": entity.externalId,
            "isActive": entity.isActive,
            "externalTeachingModalityId": entity.externalTeachingModalityId,
            "externalEducationLevelId": entity.externalEducationLevelId,
            "courseTypeId": entity.courseTypeId,
            "polo_id": entity.polo_id,
        }

        if entity.modalidade_ensino:
            data["modalidade_ensino"] = {
                "id": entity.modalidade_ensino.id,
                "status": entity.modalidade_ensino.status,
                "name": entity.modalidade_ensino.name,
                "externalId": entity.modalidade_ensino.externalId,
                "teachingModalityTypeId": entity.modalidade_ensino.teachingModalityTypeId,
            }
        if entity.nivel_ensino:
            data["nivel_ensino"] = {
                "id": entity.nivel_ensino.id,
                "status": entity.nivel_ensino.status,
                "name": entity.nivel_ensino.name,
                "externalId": entity.nivel_ensino.externalId,
                "educationLevelTypeId": entity.nivel_ensino.educationLevelTypeId,
            }
        if entity.polo:
            data["polo"] = {
                "id": entity.polo.id,
                "name": entity.polo.name,
            }

        return CursosOutput(**data)

    def to_dict(self, entity_model: CursosModel) -> dict[str, Any]:
        return {
            "id": entity_model.id,
            "name": entity_model.name,
            "externalId": entity_model.externalId,
            "isActive": entity_model.isActive,
            "courseTypeId": entity_model.courseTypeId,
            "externalTeachingModalityId": entity_model.externalTeachingModalityId,
            "externalEducationLevelId": entity_model.externalEducationLevelId,
            "polo_id": entity_model.polo_id,
        }

    def output_csv(self, all_entity: list[CursosModel]):

        if len(all_entity) <= 0:
            raise EntityNotFoundException("Nenhum registro encontrado")

        output = StringIO()

        entity_dict = [self.to_dict(x) for x in all_entity]
        df = pd.DataFrame(entity_dict)

        df = df.drop(columns=["id"])
        df = df.drop(columns=["polo_id"])
        # print(df.to_markdown(index=False))
        df.to_csv(
            output,
            index=False,
            sep=";",
            encoding="utf-8",
        )
        output.seek(0)

        return output

    async def xlsx_to_dataframe(self, file: UploadFile) -> pd.DataFrame:

        if not file.filename.endswith(".xlsx"):
            raise ValueError("O arquivo deve ser .xlsx")

        content = await file.read()

        df = pd.read_excel(
            BytesIO(content),
            engine="openpyxl",
            usecols=["POLO", "CURSO", "MODALIDADE", "externalEducationLevelId"],
        )

        return df

    async def df_remover_cursos_duplicados(self, df: pd.DataFrame):
        df_unique = df.drop_duplicates(subset=["CURSO"])
        return df_unique

    def prepare_dataframe(self, df: pd.DataFrame):
        df["name"] = df["CURSO"].apply(normalize_text)
        df["externalId"] = df["CURSO"].apply(set_externalId)
        df["isActive"] = True
        df["courseTypeId"] = df["externalId"].apply(set_courseTypeId)
        df["externalTeachingModalityId"] = df["MODALIDADE"]
        df = df.drop(columns=["CURSO"])
        df = df.rename(
            columns={"POLO": "polo_id", "MODALIDADE": "externalTeachingModalityId"}
        )
        df = df[
            [
                "name",
                "externalId",
                "isActive",
                "courseTypeId",
                "externalTeachingModalityId",
                "externalEducationLevelId",
                "polo_id",
            ]
        ]

        df["courseTypeId"] = df["courseTypeId"].astype(str)
        df["externalTeachingModalityId"] = df["externalTeachingModalityId"].astype(str)
        df["externalEducationLevelId"] = df["externalEducationLevelId"].astype(str)

        return df

    async def verify_persistence(
        self, entity: list, instance_controller: "CursosController"  # type: ignore
    ) -> list | None:

        found: list = []
        not_found: list = []

        for e in entity:
            try:
                is_exists = instance_controller.repository.find(
                    _externalId=e["externalId"]
                )

                found.append(is_exists)

            except:
                not_found.append(e)

        return [found, not_found]

    # from src.apps.cursos.cursos_controller import CursosController
    async def persist(
        self,
        entity: list,
        instance_controller: "CursosController",  # type: ignore
        update: bool = False,
    ):

        sucess: list = []
        erros: list = []

        if update is True:
            for e in entity:
                result = instance_controller.repository.edit(e.id, e)

                if result:
                    curso = {}
                    curso["id"] = result.id
                    curso["name"] = result.name
                    curso["externalId"] = result.externalId
                    curso["isActive"] = result.isActive
                    curso["courseTypeId"] = result.courseTypeId
                    curso["externalTeachingModalityId"] = (
                        result.externalTeachingModalityId
                    )
                    curso["externalEducationLevelId"] = result.externalEducationLevelId
                    curso["polo_id"] = result.polo_id

                    sucess.append(curso)
                else:
                    erros.append(e)

            return [sucess, erros]

        for e in entity:

            cursos_input = CursosInput(**e)
            result = instance_controller.create(cursos_input)

            if result:
                curso = {}
                curso["id"] = result.id
                curso["name"] = result.name
                curso["externalId"] = result.externalId
                curso["isActive"] = result.isActive
                curso["courseTypeId"] = result.courseTypeId
                curso["externalTeachingModalityId"] = result.externalTeachingModalityId
                curso["externalEducationLevelId"] = result.externalEducationLevelId
                curso["polo_id"] = result.polo_id
                sucess.append(curso)
            else:
                erros.append(e)

        return [sucess, erros]
