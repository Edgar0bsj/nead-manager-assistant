from fastapi import APIRouter, Request, Form, Response
from fastapi.responses import RedirectResponse
import httpx
from typing import Optional
from src.config import templates

router = APIRouter(prefix="/cursos")


@router.get("/", name="cursos_main")
async def find_all(request: Request):

    # url = "http://127.0.0.1:8080/nivel-ensino/"

    # async with httpx.AsyncClient() as client:
    #     response = await client.get(url=url)
    #     elements = response.json()

    return templates.TemplateResponse(
        request=request,
        name="cursos/MainPage.html",
        context={
            "data": [
                {
                    "id": 1,
                    "name": "BIOMEDICINA (Semipresencial)",
                    "externalId": "418",
                    "isActive": False,
                    "externalTeachingModalityId": "5",
                    "externalEducationLevelId": "1",
                    "courseTypeId": "technologist",
                },
                {
                    "id": 2,
                    "name": "BIOMEDICINA (Semipresencial)",
                    "externalId": "418",
                    "isActive": True,
                    "externalTeachingModalityId": "5",
                    "externalEducationLevelId": "1",
                    "courseTypeId": "technologist",
                },
                {
                    "id": 3,
                    "name": "BIOMEDICINA (Semipresencial)",
                    "externalId": "418",
                    "isActive": True,
                    "externalTeachingModalityId": "5",
                    "externalEducationLevelId": "1",
                    "courseTypeId": "technologist",
                },
                {
                    "id": 4,
                    "name": "BIOMEDICINA (Semipresencial)",
                    "externalId": "418",
                    "isActive": True,
                    "externalTeachingModalityId": "5",
                    "externalEducationLevelId": "1",
                    "courseTypeId": "technologist",
                },
            ]
        },
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

    print("////// CREATE ///////")
    print(name)
    print(externalId)
    print(isActive)
    print(externalTeachingModalityId)
    print(externalEducationLevelId)
    print(courseTypeId)

    # url = "http://127.0.0.1:8080/nivel-ensino/"

    # async with httpx.AsyncClient() as client:
    #     response = await client.get(url=url)
    #     elements = response.json()

    return RedirectResponse(url="http://127.0.0.1:8000/cursos/", status_code=303)


@router.post("/", name="cursos_delete")
async def update(
    request: Request,
    name: str = Form(...),
    externalId: str = Form(...),
    isActive: bool = Form(...),
    externalTeachingModalityId: str = Form(...),
    externalEducationLevelId: str = Form(...),
    courseTypeId: str = Form(...),
):

    print("////// UPDATE ///////")
    print(name)
    print(externalId)
    print(isActive)
    print(externalTeachingModalityId)
    print(externalEducationLevelId)
    print(courseTypeId)

    # url = "http://127.0.0.1:8080/nivel-ensino/"

    # async with httpx.AsyncClient() as client:
    #     response = await client.get(url=url)
    #     elements = response.json()

    return RedirectResponse(url="http://127.0.0.1:8000/cursos/", status_code=303)


@router.post("/delete", name="cursos_delete")
async def delete(request: Request):

    # url = "http://127.0.0.1:8080/nivel-ensino/"

    # async with httpx.AsyncClient() as client:
    #     response = await client.get(url=url)
    #     elements = response.json()

    return RedirectResponse(url="http://127.0.0.1:8000/cursos/", status_code=303)
