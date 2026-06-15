from src.apps.alt_codigo_externo.alt_codigo_externo_model import (
    AlteracaoCodigoExternoModel,
)
from src.apps.alt_codigo_externo.alt_codigo_externo_dto import (
    AlteracaoCodigoExternoInput,
    AlteracaoCodigoExternoOutput,
)
from typing import Any


class AlteracaoCodigoExternoService:
    def to_entity(
        self, dto: AlteracaoCodigoExternoInput
    ) -> AlteracaoCodigoExternoModel:
        return AlteracaoCodigoExternoModel(
            status=dto.status,
            sistema=dto.sistema,
            unidade=dto.unidade,
            entity=dto.entity,
            oldExternalId=dto.oldExternalId,
            newExternalId=dto.newExternalId,
        )

    def to_dtoOutput(self, entity: AlteracaoCodigoExternoModel):
        return AlteracaoCodigoExternoOutput(
            id=entity.id,
            status=entity.status,
            sistema=entity.sistema,
            unidade=entity.unidade,
            entity=entity.entity,
            oldExternalId=entity.oldExternalId,
            newExternalId=entity.newExternalId,
        )

    def to_dict(self, entity_model: AlteracaoCodigoExternoModel) -> dict[str, Any]:
        return {
            "id": entity_model.id,
            "status": entity_model.status,
            "sistema": entity_model.sistema,
            "unidade": entity_model.unidade,
            "entity": entity_model.entity,
            "oldExternalId": entity_model.oldExternalId,
            "newExternalId": entity_model.newExternalId,
        }
