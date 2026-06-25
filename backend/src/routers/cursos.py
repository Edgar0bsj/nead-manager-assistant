# Dependency
from fastapi import APIRouter, Depends, UploadFile, status, Path, File

# Packages
from src.apps.cursos import CursosOutput, CursosInput
from src.apps.cursos import CursosController

# //--

router = APIRouter(prefix="/cursos")


def get_depends():
    return CursosController()


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=CursosOutput,
)
def create(
    payload: CursosInput,
    controller: CursosController = Depends(get_depends),
):
    return controller.create(payload)


@router.get("/export-csv", status_code=status.HTTP_200_OK)
async def save_to_csv(
    controller: CursosController = Depends(get_depends),
):
    return controller.export_csv()


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=CursosOutput,
)
def read_one(
    id: int = Path(..., title="ID do codigo", ge=1),
    controller: CursosController = Depends(get_depends),
):
    return controller.read_one(id)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=list[CursosOutput],
)
def read_all(
    controller: CursosController = Depends(get_depends),
):
    return controller.read_all()


@router.put(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=CursosOutput,
)
def update(
    payload: CursosInput,
    id: int = Path(..., title="ID do codigo", ge=1),
    controller: CursosController = Depends(get_depends),
):
    return controller.update(id, payload)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(
    id: int = Path(..., title="ID da entidade", ge=1),
    controller: CursosController = Depends(get_depends),
):
    return controller.delete(id)


@router.post("/upload-xlsx", status_code=status.HTTP_200_OK)
async def upload_xlsx(
    file: UploadFile = File(...), controller: CursosController = Depends(get_depends)
):
    result = await controller.process_file_xlsx(file)

    return result
