from src.shared.enums import *
from fastapi import APIRouter, Form, Request
from src.shared.http_client import (
    read_entity,
    create_entity,
    update_entity,
    delete_entity,
)
from src.shared.utils import render_view, add_courses_count, redirectTo

router = APIRouter(prefix="/nivelEns")


@router.get("/", name="nivelEns_read")
async def read(req: Request):
    context = {}

    data = await read_entity(APIEndpoints.NIVEL_ENSINO.value)
    context["data"] = add_courses_count(data)

    return render_view(req, TemplatesPages.NIVEL_ENSINO.value, context)


@router.post("/create", name="nivelEns_create")
async def create(
    status: bool = Form(...),
    name: str = Form(...),
    externalId: str = Form(...),
    educationLevelTypeId: str = Form(...),
):
    payload = {
        "status": status,
        "name": name,
        "externalId": externalId,
        "educationLevelTypeId": educationLevelTypeId,
    }

    await create_entity(payload)

    return redirectTo(f"{BASE_URL}/nivelEns/")


@router.post("/update", name="nivelEns_update")
async def update(
    id: int = Form(...),
    status: bool = Form(...),
    name: str = Form(...),
    externalId: str = Form(...),
    educationLevelTypeId: str = Form(...),
):
    api = f"{APIEndpoints.NIVEL_ENSINO.value}{id}"
    payload = {
        "status": status,
        "name": name,
        "externalId": externalId,
        "educationLevelTypeId": educationLevelTypeId,
    }

    await update_entity(api, payload)

    return redirectTo(f"{BASE_URL}/nivelEns/")


@router.post("/delete", name="nivelEns_delete")
async def delete(
    request: Request,
    id: int = Form(...),
):
    api = f"{APIEndpoints.NIVEL_ENSINO.value}{id}"

    await delete_entity(api)

    return redirectTo(f"{BASE_URL}/nivelEns/")
