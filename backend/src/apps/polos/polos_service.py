# Dependency
from typing import Any

# Packages
from .polos_model import PoloModel
from .polos_dto import PoloInput, PoloOutput


class PoloService:
    def to_entity(self, dto: PoloInput) -> PoloModel:
        return PoloModel(name=dto.name)

    def to_dtoOutput(self, entity: PoloModel) -> PoloOutput:

        data = {
            "id": entity.id,
            "name": entity.name,
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

        return PoloOutput(**data)

    def to_dict(self, entity_model: PoloModel) -> dict[str, Any]:
        return {
            "id": entity_model.id,
            "name": entity_model.name,
        }
