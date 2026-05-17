from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check():

    response = client.get("/")

    assert response.status_code == 200


def test_get_metadata_missing_record():

    response = client.get(
        "/metadata?url=https://example.com"
    )

    assert response.status_code == 200