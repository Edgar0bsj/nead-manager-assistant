from fastapi import APIRouter, Request, Form, Response
from fastapi.responses import RedirectResponse
import httpx
from typing import Optional
from src.config import templates

router = APIRouter(prefix="/nivel-ensino")


@router.get("/", name="nivel_ensino")
async def find_all(request: Request):

    url = "http://127.0.0.1:8080/nivel-ensino/"

    async with httpx.AsyncClient() as client:
        response = await client.get(url=url)
        elements = response.json()

    return templates.TemplateResponse(
        request=request,
        name="nivel_ensino/MainPage.html",
        context={"data": elements},
    )


@router.post("/", name="nivel_ensino_create")
async def create(
    request: Request,
    status: bool = Form(...),
    name: str = Form(...),
    externalId: str = Form(...),
    educationLevelTypeId: str = Form(...),
):
    params = {}
    params["status"] = status
    params["name"] = name
    params["externalId"] = externalId
    params["educationLevelTypeId"] = educationLevelTypeId

    url = "http://127.0.0.1:8080/nivel-ensino/"

    async with httpx.AsyncClient() as client:
        response = await client.post(url=url, json=params)
        print(response.status_code)

    return RedirectResponse(url="http://127.0.0.1:8000/nivel-ensino/", status_code=303)


@router.post("/delete", name="nivel_ensino_delete")
async def delete(request: Request, id: int = Form(...)):

    url = f"http://127.0.0.1:8080/nivel-ensino/{id}"

    async with httpx.AsyncClient() as client:
        response = await client.delete(url=url)
        print(response.status_code)

    return RedirectResponse(url="http://127.0.0.1:8000/nivel-ensino/", status_code=303)
