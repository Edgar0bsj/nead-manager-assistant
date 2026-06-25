# Dependency
from typing import Optional
from pydantic import BaseModel


class PoloInput(BaseModel):
    name: str


class PoloOutput(BaseModel):
    id: int
    name: str

    # Campo relacionado
    cursos: Optional[list] = None
