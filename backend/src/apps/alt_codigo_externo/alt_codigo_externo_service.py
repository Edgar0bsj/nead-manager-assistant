from src.err.exceptios import EntityNotFoundException
from src.apps.alt_codigo_externo.alt_codigo_externo_model import (
    AlteracaoCodigoExternoModel,
)
from src.apps.alt_codigo_externo.alt_codigo_externo_dto import (
    AlteracaoCodigoExternoInput,
    AlteracaoCodigoExternoOutput,
)
from typing import Any
import pandas as pd
from io import StringIO


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

    def csv_export(self, all_data: list[AlteracaoCodigoExternoModel]) -> StringIO:
        if len(all_data) <= 0:
            raise EntityNotFoundException()

        output = StringIO()

        entity_dict = [self.to_dict(x) for x in all_data]
        df = pd.DataFrame(entity_dict)
        df = df.drop(columns=["id", "status", "sistema", "unidade"])

        # print(df.to_markdown(index=False))
        df.to_csv(
            output,
            index=False,
            sep=";",
            encoding="utf-8",
        )
        output.seek(0)

        return output
