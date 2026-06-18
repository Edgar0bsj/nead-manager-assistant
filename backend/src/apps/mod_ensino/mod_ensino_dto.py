from pydantic import BaseModel


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
