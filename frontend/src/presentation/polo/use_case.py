from fastapi import Request
from fastapi.responses import RedirectResponse
from starlette.templating import _TemplateResponse
from starlette.responses import RedirectResponse
from src.shared import templating
import httpx


def render_polo(request: Request, name: str, context: dict) -> _TemplateResponse:

    return templating().TemplateResponse(request=request, name=name, context=context)


def redirectTo(url: str, status_code=303) -> RedirectResponse:
    return RedirectResponse(url=url, status_code=status_code)


async def get_polos(url: str) -> list:

    async with httpx.AsyncClient() as client:
        response = await client.get(url=url)
        elements = response.json()
        return elements
