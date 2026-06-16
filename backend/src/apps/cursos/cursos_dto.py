from pydantic import BaseModel


class CursoInput(BaseModel):
    status: bool
    sistema: str
    unidade: str
    name: str
    externalId: str
    isActive: bool
    externalTeachingModalityId: str
    externalEducationLevelId: str
    courseTypeId: str


class CursoOutput(BaseModel):
    id: int
    status: bool
    sistema: str
    unidade: str
    name: str
    externalId: str
    isActive: bool
    externalTeachingModalityId: str
    externalEducationLevelId: str
    courseTypeId: str
