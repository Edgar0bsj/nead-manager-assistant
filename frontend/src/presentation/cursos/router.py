from fastapi import APIRouter, Form, Request
from src.shared.enums import BASE_URL, APIEndpoints, TemplatesPages
from src.shared.utils import redirectTo, render_view
from src.shared.http_client import (
    read_entity,
    create_entity,
    update_entity,
    delete_entity,
)

router = APIRouter(prefix="/cursos")


@router.get("/", name="cursos_read")
async def read(req: Request):
    context = {}

    context["data"] = await read_entity(APIEndpoints.CURSOS.value)

    return render_view(req, TemplatesPages.CURSOS.value, context)


@router.post("/create", name="cursos_create")
async def create(
    name: str = Form(...),
    externalId: str = Form(...),
    isActive: bool = Form(...),
    courseTypeId: str = Form(...),
    externalTeachingModalityId: str = Form(...),
    externalEducationLevelId: str = Form(...),
    polo_id: int = Form(...),
):
    payload = {
        "name": name,
        "externalId": externalId,
        "isActive": isActive,
        "courseTypeId": courseTypeId,
        "externalTeachingModalityId": externalTeachingModalityId,
        "externalEducationLevelId": externalEducationLevelId,
        "polo_id": polo_id,
    }

    await create_entity(APIEndpoints.CURSOS.value, payload)

    return redirectTo(f"{BASE_URL}/cursos/")


@router.post("/update", name="cursos_update")
async def update(
    id: int = Form(...),
    name: str = Form(...),
    externalId: str = Form(...),
    isActive: bool = Form(...),
    courseTypeId: str = Form(...),
    externalTeachingModalityId: str = Form(...),
    externalEducationLevelId: str = Form(...),
    polo_id: int = Form(...),
):
    api = f"{APIEndpoints.CURSOS.value}{id}"
    payload = {
        "name": name,
        "externalId": externalId,
        "isActive": isActive,
        "courseTypeId": courseTypeId,
        "externalTeachingModalityId": externalTeachingModalityId,
        "externalEducationLevelId": externalEducationLevelId,
        "polo_id": polo_id,
    }

    await update_entity(api, payload)

    return redirectTo(f"{BASE_URL}/cursos/")


@router.post("/delete", name="cursos_delete")
async def delete(
    id: int = Form(...),
):
    api = f"{APIEndpoints.CURSOS.value}{id}"

    await delete_entity(api)

    return redirectTo(f"{BASE_URL}/cursos/")
