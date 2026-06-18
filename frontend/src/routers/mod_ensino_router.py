from fastapi import APIRouter, Request, Form, Response
from fastapi.responses import RedirectResponse
import httpx
from typing import Optional
from src.config import templates

router = APIRouter(prefix="/mod-ensino")


@router.get("/", name="mod_ensino")
async def find_all(request: Request, msg: Optional[str] = None):

    url = "http://127.0.0.1:8080/mods-ensino/"

    async with httpx.AsyncClient() as client:
        response = await client.get(url=url)
        response = response.json()

    return templates.TemplateResponse(
        request=request,
        name="modalidades_ensino/MainPage.html",
        context={"data": response, "msg_errs": msg},
    )


@router.post("/", name="mod_ensino_add")
async def create(
    request: Request,
    status: str = Form(...),
    name: str = Form(...),
    type_modali: str = Form(...),
    externalId: str = Form(...),
):
    status = True if status == "true" else False
    params = {}
    params["status"] = status
    params["name"] = name
    params["externalId"] = externalId
    params["teachingModalityTypeId"] = type_modali

    url = "http://127.0.0.1:8080/mods-ensino/"

    async with httpx.AsyncClient() as client:
        response = await client.post(url=url, json=params)

        msg_response = "/"
        if response.status_code == 201:
            msg_response = "Modalidade de ensino criado com sucesso!"
        if response.status_code == 409:
            msg_response = "Erro na criação, Modalidade de ensino já existe na base de dados com esse codigo de externo"

    return RedirectResponse(
        url=f"http://127.0.0.1:8000/mod-ensino/?msg={msg_response}", status_code=303
    )


@router.post("/delete", name="mod_ensino_del")
async def delete(
    request: Request,
    id: int = Form(...),
):
    url = f"http://127.0.0.1:8080/mods-ensino/{id}"
    print(url)

    async with httpx.AsyncClient() as client:
        response = await client.delete(url=url)
        print(response.status_code)

    return RedirectResponse(url="http://127.0.0.1:8000/mod-ensino", status_code=303)


@router.post("/update", name="mod_ensino_update")
async def update(
    request: Request,
    id: int = Form(...),
    status: str = Form(...),
    name: str = Form(...),
    type_modali: str = Form(...),
    externalId: str = Form(...),
):
    status = True if status == "true" else False

    params = {}
    params["status"] = status
    params["name"] = name
    params["externalId"] = externalId
    params["teachingModalityTypeId"] = type_modali

    url = f"http://127.0.0.1:8080/mods-ensino/{id}"

    async with httpx.AsyncClient() as client:
        response = await client.post(url=url, json=params)

    msg_response = None
    if response.status_code == 201:
        msg_response = "Modalidade de ensino criado com sucesso!"
    if response.status_code == 409:
        msg_response = "Erro na criação, Modalidade de ensino já existe na base de dados com esse codigo de externo"

    url = (
        f"http://127.0.0.1:8000/mod-ensino/?msg={msg_response}"
        if msg_response is not None
        else "http://127.0.0.1:8000/mod-ensino/"
    )
    return RedirectResponse(url=url, status_code=303)
