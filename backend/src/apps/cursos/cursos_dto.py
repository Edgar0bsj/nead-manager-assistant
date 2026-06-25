# Dependency
from pydantic import BaseModel
from typing import Optional


class CursosInput(BaseModel):
    name: str
    externalId: str
    isActive: bool
    courseTypeId: str
    externalTeachingModalityId: str
    externalEducationLevelId: str
    polo_id: int


class CursosOutput(BaseModel):
    id: int
    name: str
    externalId: str
    isActive: bool
    externalTeachingModalityId: str
    externalEducationLevelId: str
    courseTypeId: str
    polo_id: int

    # Campos relacionados
    modalidade_ensino: Optional[dict] = None
    nivel_ensino: Optional[dict] = None
    polo: Optional[dict] = None
