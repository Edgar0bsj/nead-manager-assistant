from datetime import date

from pydantic import BaseModel


class AlteracaoCodigoExternoInput(BaseModel):
    status: bool
    sistema: str
    unidade: str
    entity: str
    oldExternalId: str
    newExternalId: str


class AlteracaoCodigoExternoOutput(BaseModel):
    id: int
    status: bool
    sistema: str
    unidade: str
    entity: str
    oldExternalId: str
    newExternalId: str
