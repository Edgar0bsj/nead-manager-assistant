from fastapi import APIRouter, Request, Form, Response
from fastapi.responses import RedirectResponse
import httpx
from typing import Optional
from src.shared import templating

router = APIRouter(prefix="/cursos")


@router.get("/", name="cursos_main")
async def find_all(request: Request):

    url = "http://127.0.0.1:8080/cursos/"

    async with httpx.AsyncClient() as client:
        response = await client.get(url=url)
        elements = response.json()

    return templating().TemplateResponse(
        request=request,
        name="cursos/MainPage.html",
        context={"data": elements},
    )


@router.post("/", name="cursos_create")
async def create(
    request: Request,
    name: str = Form(...),
    externalId: str = Form(...),
    isActive: bool = Form(...),
    externalTeachingModalityId: str = Form(...),
    externalEducationLevelId: str = Form(...),
    courseTypeId: str = Form(...),
):

    params = {
        "name": name,
        "externalId": externalId,
        "isActive": isActive,
        "externalTeachingModalityId": externalTeachingModalityId,
        "externalEducationLevelId": externalEducationLevelId,
        "courseTypeId": courseTypeId,
    }

    url = "http://127.0.0.1:8080/cursos/"

    async with httpx.AsyncClient() as client:
        response = await client.post(url=url, json=params)
        print(response.status_code)

    return RedirectResponse(url="http://127.0.0.1:8000/cursos/", status_code=303)


@router.post("/update", name="cursos_update")
async def update(
    request: Request,
    id: int = Form(...),
    name: str = Form(...),
    externalId: str = Form(...),
    isActive: bool = Form(...),
    externalTeachingModalityId: str = Form(...),
    externalEducationLevelId: str = Form(...),
    courseTypeId: str = Form(...),
):

    params = {
        "name": name,
        "externalId": externalId,
        "isActive": isActive,
        "externalTeachingModalityId": externalTeachingModalityId,
        "externalEducationLevelId": externalEducationLevelId,
        "courseTypeId": courseTypeId,
    }

    url = f"http://127.0.0.1:8080/cursos/{id}"

    async with httpx.AsyncClient() as client:
        response = await client.put(url=url, json=params)
        print(response.status_code)

    return RedirectResponse(url="http://127.0.0.1:8000/cursos/", status_code=303)


@router.post("/delete", name="cursos_delete")
async def delete(
    request: Request,
    id: int = Form(...),
):

    url = f"http://127.0.0.1:8080/cursos/{id}"

    async with httpx.AsyncClient() as client:
        response = await client.delete(url=url)
        print(response.status_code)

    return RedirectResponse(url="http://127.0.0.1:8000/cursos/", status_code=303)
