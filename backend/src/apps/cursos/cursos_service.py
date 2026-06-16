from src.apps.cursos.cursos_model import CursosModel
from src.apps.cursos.cursos_dto import CursoInput, CursoOutput
from typing import Any


class CursoService:
    def to_entity(self, dto: CursoInput) -> CursosModel:
        return CursosModel(
            status=dto.status,
            sistema=dto.sistema,
            unidade=dto.unidade,
            name=dto.name,
            externalId=dto.externalId,
            isActive=dto.isActive,
            externalTeachingModalityId=dto.externalTeachingModalityId,
            externalEducationLevelId=dto.externalEducationLevelId,
            courseTypeId=dto.courseTypeId,
        )

    def to_dtoOutput(self, entity: CursosModel):
        return CursoOutput(
            id=entity.id,
            status=entity.status,
            sistema=entity.sistema,
            unidade=entity.unidade,
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
            "status": entity_model.status,
            "sistema": entity_model.sistema,
            "unidade": entity_model.unidade,
            "name": entity_model.name,
            "externalId": entity_model.externalId,
            "isActive": entity_model.isActive,
            "externalTeachingModalityId": entity_model.externalTeachingModalityId,
            "externalEducationLevelId": entity_model.externalEducationLevelId,
            "courseTypeId": entity_model.courseTypeId,
        }
