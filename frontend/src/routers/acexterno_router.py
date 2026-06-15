from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse
from src.config import templates
import httpx

from src.util.parser_date_format import parser_date_format

router = APIRouter(prefix="/acexterno", tags=["ACExterno"])


@router.get("/", name="acexterno")
async def find_all(request: Request):
    async with httpx.AsyncClient() as client:
        requisicao = await client.get(
            "http://127.0.0.1:8080/alt-codigo-externo/", timeout=10
        )

        result = requisicao.json()
        data = [
            {
                "id": e["id"],
                "data": parser_date_format(e["data"]),
                "sistema": e["sistema"],
                "unidade": e["unidade"],
                "name": e["name"],
                "oldExternalId": e["oldExternalId"],
                "newExternalId": e["newExternalId"],
            }
            for e in result
        ]

        return templates.TemplateResponse(
            request=request,
            name="alt_codigo_externo/alt_codigo_externo_index.html",
            context={"notificacao": "...", "dados": data},
        )


@router.post("/create-add", name="create_add_acexterno")
async def create_add(
    request: Request,
    sistema: str = Form(...),
    unidade: str = Form(...),
    name: str = Form(...),
    oldExternalId: str = Form(...),
    newExternalId: str = Form(...),
):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://127.0.0.1:8080/alt-codigo-externo/create",
            json={
                "sistema": sistema,
                "unidade": unidade,
                "name": name,
                "oldExternalId": oldExternalId,
                "newExternalId": newExternalId,
            },
        )
        print(response.status_code)

    return RedirectResponse(url="http://127.0.0.1:8000/acexterno/", status_code=303)


@router.get("/delete/{id}", name="alt_cod_exter_delete")
async def delete(request: Request, id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "http://127.0.0.1:8080/alt-codigo-externo/delete", params={"id": id}
        )

    print(response.status_code)
    return RedirectResponse(url="http://127.0.0.1:8000/acexterno/", status_code=303)


@router.post("/update", name="update_acexterno")
async def update(
    request: Request,
    id: int = Form(...),
    sistema: str = Form(...),
    unidade: str = Form(...),
    name: str = Form(...),
    oldExternalId: str = Form(...),
    newExternalId: str = Form(...),
):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"http://127.0.0.1:8080/alt-codigo-externo/update/{id}",
            json={
                "sistema": sistema,
                "unidade": unidade,
                "name": name,
                "oldExternalId": oldExternalId,
                "newExternalId": newExternalId,
            },
        )
        print(response.status_code)

    return RedirectResponse(url="http://127.0.0.1:8000/acexterno/", status_code=303)
