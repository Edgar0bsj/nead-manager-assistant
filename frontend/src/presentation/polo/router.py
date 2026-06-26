from fastapi import APIRouter, Form, Request
from .use_case import render_polo, redirectTo, get_polos
from .effects import create_polo, delete_polo, update_polo

router = APIRouter(prefix="/polos")


@router.get("/", name="polos_read")
async def read(req: Request):

    url = "http://127.0.0.1:8080/polo/"

    data = await get_polos(url)
    print(data)

    return render_polo(req, "polos/MainPage.html", {"data": data})


@router.post("/create", name="polos_create")
async def create(req: Request, name: str = Form(...)):

    status_code = await create_polo(name, "http://127.0.0.1:8080/polo")

    return redirectTo("http://127.0.0.1:8000/polos")


@router.post("/update", name="polos_update")
async def update(
    request: Request,
    id: str = Form(...),
    name: str = Form(...),
):

    status_code = await update_polo(id, name, "http://127.0.0.1:8000/polos")

    return redirectTo("http://127.0.0.1:8000/polos")


@router.post("/delete", name="polos_delete")
async def delete(
    request: Request,
    id: str = Form(...),
):

    status_code = await delete_polo(id, "http://127.0.0.1:8000/polos")

    return redirectTo("http://127.0.0.1:8000/polos/")
