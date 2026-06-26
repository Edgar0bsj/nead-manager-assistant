from typing import Any
from httpx import AsyncClient


async def create_polo(name: str, url: str) -> int:
    _json = {"name": name}

    async with AsyncClient() as client:
        response = await client.post(url=url, json=_json)

        return response.status_code


async def update_polo(id: int, name: str, url: str) -> int:
    _url = f"{url}/{id}"
    _json = {"name": name}

    async with AsyncClient() as client:
        response = await client.put(url=_url, json=_json)

        return response.status_code


async def delete_polo(id: int, url: str) -> int:
    _url = f"{url}/{id}"
    async with AsyncClient() as client:
        response = await client.delete(url=_url)

        return response.status_code
