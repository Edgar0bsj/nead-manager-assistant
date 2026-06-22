from pydantic import BaseModel
from typing import Optional, Any


class CursosInput(BaseModel):
    name: str
    externalId: str
    isActive: bool
    externalTeachingModalityId: str
    externalEducationLevelId: str
    courseTypeId: str


class CursosOutput(BaseModel):
    id: int
    name: str
    externalId: str
    isActive: bool
    externalTeachingModalityId: str
    externalEducationLevelId: str
    courseTypeId: str

    # Campos relacionados
    modalidade_ensino: Optional[dict] = None
    nivel_ensino: Optional[dict] = None
