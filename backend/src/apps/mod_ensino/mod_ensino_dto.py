from pydantic import BaseModel
from typing import Optional


class ModEnsinoInput(BaseModel):
    status: bool
    name: str
    externalId: str
    teachingModalityTypeId: str


class ModEnsinoOutput(BaseModel):
    id: int
    status: bool
    name: str
    externalId: str
    teachingModalityTypeId: str

    cursos: Optional[list] = None
