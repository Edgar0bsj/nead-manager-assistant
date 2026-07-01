from src.shared.enums import BASE_URL, APIEndpoints, TemplatesPages
from fastapi import APIRouter, Form, Request
from src.shared.utils import redirectTo, render_view, add_courses_count
from src.shared.http_client import (
    read_entity,
    create_entity,
    update_entity,
    delete_entity,
)

router = APIRouter(prefix="/modEnsino")


@router.get("/", name="modEnsino_read")
async def read(req: Request):
    context = {}

    data = await read_entity(APIEndpoints.MODALIDADE_ENSINO.value)
    context["data"] = add_courses_count(data)

    return render_view(req, TemplatesPages.MODALIDADE_ENSINO.value, context)


@router.post("/create", name="modEnsino_create")
async def create(
    req: Request,
    status: bool = Form(...),
    name: str = Form(...),
    externalId: str = Form(...),
    teachingModalityTypeId: str = Form(...),
):
    payload = {
        "status": status,
        "name": name,
        "externalId": externalId,
        "teachingModalityTypeId": teachingModalityTypeId,
    }

    await create_entity(APIEndpoints.MODALIDADE_ENSINO.value, payload)

    return redirectTo(f"{BASE_URL}/modEnsino")


@router.post("/update", name="modEnsino_update")
async def update(
    id: str = Form(...),
    status: bool = Form(...),
    name: str = Form(...),
    externalId: str = Form(...),
    teachingModalityTypeId: str = Form(...),
):
    api = f"{APIEndpoints.MODALIDADE_ENSINO.value}{id}"
    payload = {
        "status": status,
        "name": name,
        "externalId": externalId,
        "teachingModalityTypeId": teachingModalityTypeId,
    }

    await update_entity(api, payload)

    return redirectTo(f"{BASE_URL}/modEnsino")


@router.post("/delete", name="modEnsino_delete")
async def delete(
    id: int = Form(...),
):
    api = f"{APIEndpoints.MODALIDADE_ENSINO.value}{id}"

    await delete_entity(api)

    return redirectTo(f"{BASE_URL}/modEnsino")
