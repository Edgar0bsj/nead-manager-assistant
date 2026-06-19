from fastapi import APIRouter, Request, Form, Response
from fastapi.responses import RedirectResponse
import httpx
from typing import Optional
from src.config import templates

router = APIRouter(prefix="/nivel-ensino")


@router.get("/", name="nivel_ensino")
async def find_all(request: Request):

    # url = "http://127.0.0.1:8080/mods-ensino/"

    # async with httpx.AsyncClient() as client:
    #     response = await client.get(url=url)
    #     response = response.json()

    return templates.TemplateResponse(
        request=request,
        name="nivel_ensino/MainPage.html",
        context={"data": {}},
    )
