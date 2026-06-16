from src.apps.nivel_ensino.nivel_ensino_model import NivelEnsinoModel
from src.apps.nivel_ensino.nivel_ensino_dto import NivelEnsinoOutput, NivelEnsinoInput
from typing import Any


class NivelEnsinoService:
    def to_entity(self, dto: NivelEnsinoInput) -> NivelEnsinoModel:
        return NivelEnsinoModel(
            status=dto.status,
            sistema=dto.sistema,
            unidade=dto.unidade,
            name=dto.name,
            externalId=dto.externalId,
            educationLevelTypeId=dto.educationLevelTypeId,
        )

    def to_dtoOutput(self, entity: NivelEnsinoModel):
        return NivelEnsinoOutput(
            id=entity.id,
            status=entity.status,
            sistema=entity.sistema,
            unidade=entity.unidade,
            name=entity.name,
            externalId=entity.externalId,
            educationLevelTypeId=entity.educationLevelTypeId,
        )

    def to_dict(self, entity_model: NivelEnsinoModel) -> dict[str, Any]:
        return {
            "id": entity_model.id,
            "status": entity_model.status,
            "sistema": entity_model.sistema,
            "unidade": entity_model.unidade,
            "name": entity_model.name,
            "externalId": entity_model.externalId,
            "educationLevelTypeId": entity_model.educationLevelTypeId,
        }
