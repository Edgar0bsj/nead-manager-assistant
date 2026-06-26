from fastapi import APIRouter, Request, Form, Response
from fastapi.responses import RedirectResponse
import httpx
from typing import Optional

from src.presentation.polo.use_case import render_polo, redirectTo, get_polos
from src.presentation.polo.effects import create_polo, update_polo, delete_polo

router = APIRouter(prefix="/polos")


@router.get("/", name="polos")
async def find_all(
    request: Request,
):

    # await create_polo("teste100", "http://127.0.0.1:8080/polo/")
    # await update_polo(4, "Cidade nova", "http://127.0.0.1:8080/polo")
    # await delete_polo(4, "http://127.0.0.1:8080/polo")

    dados = await get_polos("http://127.0.0.1:8080/polo/")

    return render_polo(request, "polos/MainPage.html", {"data": dados})


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

    # <class 'starlette.responses.RedirectResponse'>

    return redirectTo("http://127.0.0.1:8000/polos/")


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

    return redirectTo("http://127.0.0.1:8000/polos/")


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

    return redirectTo("http://127.0.0.1:8000/polos/")
