from fastapi import APIRouter, Request, Form, Response
from fastapi.responses import RedirectResponse
from src.config import templates
import httpx
from src.util.format_status import format_status
from typing import Optional

router = APIRouter(prefix="/polos")


@router.get("/", name="polos")
async def find_all(
    request: Request,
):

    return templates.TemplateResponse(
        request=request,
        name="polos/MainPage.html",
        context={"data": {}},
    )


@router.post("/", name="polos_create")
async def create(
    request: Request,
    nome: str = Form(...),
):
    print("============== CREATE ==============")
    print(nome)
    print("============== // CREATE ==============")

    # url = f"http://127.0.0.1:8080/cursos/{id}"

    # async with httpx.AsyncClient() as client:
    #     response = await client.delete(url=url)
    #     print(response.status_code)

    return RedirectResponse(url="http://127.0.0.1:8000/polos/", status_code=303)


@router.post("/update", name="polos_update")
async def update(
    request: Request,
    id: str = Form(...),
    nome: str = Form(...),
):

    print("============== UPDATE ==============")
    print(id)
    print(nome)
    print("============== // UPDATE ==============")

    # url = f"http://127.0.0.1:8080/cursos/{id}"

    # async with httpx.AsyncClient() as client:
    #     response = await client.delete(url=url)
    #     print(response.status_code)

    return RedirectResponse(url="http://127.0.0.1:8000/polos/", status_code=303)


@router.post("/delete", name="polos_delete")
async def delete(
    request: Request,
    id: int = Form(...),
):
    print("============== DELETE ==============")
    print(id)
    print("============== // DELETE ==============")

    # url = f"http://127.0.0.1:8080/cursos/{id}"

    # async with httpx.AsyncClient() as client:
    #     response = await client.delete(url=url)
    #     print(response.status_code)

    return RedirectResponse(url="http://127.0.0.1:8000/polos/", status_code=303)
