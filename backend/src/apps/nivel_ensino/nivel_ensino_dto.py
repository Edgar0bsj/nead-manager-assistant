from pydantic import BaseModel


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
