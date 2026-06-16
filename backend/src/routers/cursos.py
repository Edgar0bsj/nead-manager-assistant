from typing import Optional
from fastapi import APIRouter, Depends, status, Path
from src.apps.cursos.cursos_dto import CursoInput, CursoOutput
from src.apps.cursos.cursos_controller import CursoController

router = APIRouter(prefix="/cursos")


def get_depends():
    return CursoController()


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=CursoOutput,
)
def create(
    payload: CursoInput,
    controller: CursoController = Depends(get_depends),
):
    return controller.create(payload)


@router.get("/to-csv", status_code=status.HTTP_200_OK)
def save_to_csv(
    filter_status: Optional[bool] = True,
    filter_sistema: Optional[str] = None,
    filter_unidade: Optional[str] = None,
    controller: CursoController = Depends(get_depends),
):
    return controller.save_to_csv(filter_status, filter_sistema, filter_unidade)


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=CursoOutput,
)
def read_one(
    id: int = Path(..., title="ID do codigo", ge=1),
    controller: CursoController = Depends(get_depends),
):
    return controller.read_one(id)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=list[CursoOutput],
)
def read_all(
    name_entity: Optional[str] = None,
    controller: CursoController = Depends(get_depends),
):
    return controller.read_all(name_entity)


@router.post(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=CursoOutput,
)
def update(
    payload: CursoInput,
    id: int = Path(..., title="ID do codigo", ge=1),
    controller: CursoController = Depends(get_depends),
):
    return controller.update(id, payload)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(
    id: int = Path(..., title="ID da entidade", ge=1),
    controller: CursoController = Depends(get_depends),
):
    return controller.delete(id)
