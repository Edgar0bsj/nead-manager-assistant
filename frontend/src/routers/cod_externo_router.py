from fastapi import APIRouter, Request, Form, Response
from fastapi.responses import RedirectResponse
from src.config import templates
import httpx
from src.util.format_status import format_status
from typing import Optional

router = APIRouter(prefix="/cod-externo")


@router.get("/", name="cod_externo")
async def find_all(
    request: Request,
    filter_status: Optional[str] = None,
    filter_sistema: Optional[str] = None,
    filter_unidade: Optional[str] = None,
    filter_entity: Optional[str] = None,
):
    params = {}

    if filter_status:
        params["status_filter"] = filter_status

    if filter_sistema:
        params["sistema_filter"] = filter_sistema

    if filter_unidade:
        params["unidade_filter"] = filter_unidade

    if filter_entity:
        params["entity_filter"] = filter_entity

    url = "http://127.0.0.1:8080/alt-codigos-externos/"

    async with httpx.AsyncClient() as client:
        response = await client.get(url=url, params=params)
        response = response.json()

        data = [
            {
                "id": x["id"],
                "status": format_status(x["status"]),
                "sistema": x["sistema"],
                "unidade": x["unidade"],
                "entity": x["entity"],
                "oldExternalId": x["oldExternalId"],
                "newExternalId": x["newExternalId"],
            }
            for x in response
        ]

    return templates.TemplateResponse(
        request=request,
        name="alt_codigo_externo/MainPage.html",
        context={"data": data, "download_filters": params},
    )


@router.post("/", name="cod_externo_create")
async def create(
    request: Request,
    status: str = Form(...),
    sistema: str = Form(...),
    unidade: str = Form(...),
    entity: str = Form(...),
    oldExternalId: str = Form(...),
    newExternalId: str = Form(...),
):
    status = True if status == "true" else False
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://127.0.0.1:8080/alt-codigos-externos/",
            json={
                "status": status,
                "sistema": sistema,
                "unidade": unidade,
                "entity": entity,
                "oldExternalId": oldExternalId,
                "newExternalId": newExternalId,
            },
        )
        print(response.status_code)

    return RedirectResponse(url="http://127.0.0.1:8000/cod-externo/", status_code=303)


@router.post("/update", name="cod_externo_update")
async def update(
    request: Request,
    id: str = Form(...),
    status: str = Form(...),
    sistema: str = Form(...),
    unidade: str = Form(...),
    entity: str = Form(...),
    oldExternalId: str = Form(...),
    newExternalId: str = Form(...),
):
    status = True if status == "true" else False

    async with httpx.AsyncClient() as client:
        response = await client.put(
            f"http://127.0.0.1:8080/alt-codigos-externos/{id}",
            json={
                "status": status,
                "sistema": sistema,
                "unidade": unidade,
                "entity": entity,
                "oldExternalId": oldExternalId,
                "newExternalId": newExternalId,
            },
        )
    print(response.status_code)

    return RedirectResponse(url="http://127.0.0.1:8000/cod-externo/", status_code=303)


@router.get("/delete/{id}")
async def delete(request: Request, id: int):

    async with httpx.AsyncClient() as client:
        response = await client.delete(
            f"http://127.0.0.1:8080/alt-codigos-externos/{id}"
        )
    print(response.status_code)

    return RedirectResponse(url="http://127.0.0.1:8000/cod-externo/", status_code=303)


@router.get("/export-csv", name="cod_externo_csv")
async def export_csv(
    request: Request,
    filter_status: Optional[str] = None,
    filter_sistema: Optional[str] = None,
    filter_unidade: Optional[str] = None,
    filter_entity: Optional[str] = None,
):
    filters = {}

    if filter_status != "":
        filters["status_filter"] = filter_status

    if filter_sistema != "":
        filters["sistema_filter"] = filter_sistema

    if filter_unidade != "":
        filters["unidade_filter"] = filter_unidade

    if filter_entity != "":
        filters["entity_filter"] = filter_entity

    async with httpx.AsyncClient() as client:
        response = await client.get(
            "http://127.0.0.1:8080/alt-codigos-externos/to-csv", params=filters
        )

    return Response(
        content=response.content,
        media_type=response.headers.get("content-type"),
        headers={"Content-Disposition": response.headers.get("content-disposition")},
    )
