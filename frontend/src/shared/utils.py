from fastapi import Request
from fastapi.responses import RedirectResponse
from starlette.templating import _TemplateResponse
from starlette.responses import RedirectResponse
from src.shared import templating


def render_view(request: Request, name: str, context: dict) -> _TemplateResponse:

    return templating().TemplateResponse(request=request, name=name, context=context)


def redirectTo(url: str, status_code=303) -> RedirectResponse:
    return RedirectResponse(url=url, status_code=status_code)


def add_courses_count(
    data: list, camp_caurso: str = "cursos", newCamp: str = "size_courses"
):
    _data = data.copy()
    for i in _data:
        if not i[camp_caurso]:
            i[newCamp] = 0
            continue

        i[newCamp] = len(i[camp_caurso])

    return _data
