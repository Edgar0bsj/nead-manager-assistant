from src.shared.enums import *
from fastapi import APIRouter, Form, Request
from src.shared.utils import add_courses_count, render_view, redirectTo
from src.shared import (
    read_entity,
    create_entity,
    update_entity,
    delete_entity,
)

router = APIRouter(prefix="/polos")


@router.get("/", name="polos_read")
async def read(req: Request):
    context = {}

    data = await read_entity(APIEndpoints.POLO.value)
    context["data"] = add_courses_count(data)

    return render_view(req, TemplatesPages.POLO.value, context)


@router.post("/create", name="polos_create")
async def create(name: str = Form(...)):

    await create_entity(APIEndpoints.POLO.value, {"name": name})

    return redirectTo(f"{BASE_URL}/polos")


@router.post("/update", name="polos_update")
async def update(
    id: str = Form(...),
    name: str = Form(...),
):

    await update_entity(f"{APIEndpoints.POLO.value}{id}", {"name": name})

    return redirectTo(f"{BASE_URL}/polos")


@router.post("/delete", name="polos_delete")
async def delete(
    id: int = Form(...),
):

    await delete_entity(f"{APIEndpoints.POLO.value}{id}")

    return redirectTo(f"{BASE_URL}/polos")
