from pydantic import BaseModel
from typing import Optional


class NivelEnsinoInput(BaseModel):
    status: bool
    name: str
    externalId: str
    educationLevelTypeId: str


class NivelEnsinoOutput(BaseModel):
    id: int
    status: bool
    name: str
    externalId: str
    educationLevelTypeId: str

    cursos: Optional[list] = None
