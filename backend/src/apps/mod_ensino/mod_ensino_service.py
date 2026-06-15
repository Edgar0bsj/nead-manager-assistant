from src.apps.mod_ensino.mod_ensino_model import ModEnsinoModel
from src.apps.mod_ensino.mod_ensino_dto import ModEnsinoInput, ModEnsinoOutput
from typing import Any


class ModEnsinoService:
    def to_entity(self, dto: ModEnsinoInput) -> ModEnsinoModel:
        return ModEnsinoModel(
            status=dto.status,
            sistema=dto.sistema,
            unidade=dto.unidade,
            name=dto.name,
            externalId=dto.externalId,
            teachingModalityTypeId=dto.teachingModalityTypeId,
        )

    def to_dtoOutput(self, entity: ModEnsinoModel):
        return ModEnsinoOutput(
            id=entity.id,
            status=entity.status,
            sistema=entity.sistema,
            unidade=entity.unidade,
            name=entity.name,
            externalId=entity.externalId,
            teachingModalityTypeId=entity.teachingModalityTypeId,
        )

    def to_dict(self, entity_model: ModEnsinoModel) -> dict[str, Any]:
        return {
            "id": entity_model.id,
            "status": entity_model.status,
            "sistema": entity_model.sistema,
            "unidade": entity_model.unidade,
            "name": entity_model.name,
            "externalId": entity_model.externalId,
            "teachingModalityTypeId": entity_model.teachingModalityTypeId,
        }
