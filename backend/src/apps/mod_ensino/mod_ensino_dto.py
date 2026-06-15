from pydantic import BaseModel


class ModEnsinoInput(BaseModel):
    status: bool
    sistema: str
    unidade: str
    name: str
    externalId: str
    teachingModalityTypeId: str


class ModEnsinoOutput(BaseModel):
    id: int
    status: bool
    sistema: str
    unidade: str
    name: str
    externalId: str
    teachingModalityTypeId: str
