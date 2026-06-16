from fastapi.testclient import TestClient
import pytest
from src.main import app

client = TestClient(app)


@pytest.mark.skip(reason="Ignorando por hora")
def test_create():
    payload = {
        "status": True,
        "sistema": "sophia",
        "unidade": "nova iguacu",
        "entity": "campus",
        "oldExternalId": "123456",
        "newExternalId": "654321",
    }
    response = client.post("/alt-codigos-externos/", json=payload)

    assert response.status_code == 201


@pytest.mark.skip(reason="Ignorando por hora")
def test_read_all():
    response = client.get("/alt-codigos-externos/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) >= 1


@pytest.mark.skip(reason="Ignorando por hora")
def test_read_one():
    response = client.get("/alt-codigos-externos/1")

    assert response.status_code == 200
    assert isinstance(response.json(), dict)


@pytest.mark.skip(reason="Ignorando por hora")
def test_update():
    all_entitys = client.get("/alt-codigos-externos/")
    entity = all_entitys.json()[-1]

    id = entity["id"]
    payload = {
        "id": entity["id"],
        "status": entity["status"],
        "sistema": entity["sistema"],
        "unidade": "Cidade Nova",
        "entity": entity["entity"],
        "oldExternalId": entity["oldExternalId"],
        "newExternalId": entity["newExternalId"],
    }

    response = client.put(f"/alt-codigos-externos/{id}", json=payload)

    assert response.status_code == 200
    assert isinstance(response.json(), dict)


@pytest.mark.skip(reason="Ignorando por hora")
def test_delete():
    # all_entitys = client.get("/alt-codigos-externos/")
    # entity = all_entitys.json()[-1]

    # id = entity["id"]

    response = client.delete(f"/alt-codigos-externos/{8}")

    assert response.status_code == 204
