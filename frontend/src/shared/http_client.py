from httpx import AsyncClient
import httpx


async def read_entity(url: str) -> list:

    async with httpx.AsyncClient() as client:
        response = await client.get(url=url)
        elements = response.json()
        return elements


async def create_entity(url: str, json: dict) -> int:

    async with AsyncClient() as client:
        response = await client.post(url=url, json=json)

        return response.status_code


async def update_entity(url: str, json: dict) -> int:

    async with AsyncClient() as client:
        response = await client.put(url=url, json=json)

        return response.status_code


async def delete_entity(url: str) -> int:

    async with AsyncClient() as client:
        response = await client.delete(url=url)

        return response.status_code
