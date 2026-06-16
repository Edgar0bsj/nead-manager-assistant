from pydantic import BaseModel


class NivelEnsinoInput(BaseModel):
    status: bool
    sistema: str
    unidade: str
    name: str
    externalId: str
    educationLevelTypeId: str


class NivelEnsinoOutput(BaseModel):
    id: int
    status: bool
    sistema: str
    unidade: str
    name: str
    externalId: str
    educationLevelTypeId: str
