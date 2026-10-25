from fastapi.testclient import TestClient

from backend.main import app


client = TestClient(app)


def test_home():

    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["project"] == "SecureSense AI"


def test_scan_api():

    response = client.post(
        "/scan",
        json={"url": "https://httpbin.org/get"}
    )

    assert response.status_code == 200

    data = response.json()

    assert data["url"] == "https://httpbin.org/get"
    assert "status_code" in data
    assert "response_time" in data
    assert "security_analysis" in data
    assert "https_analysis" in data
    assert "anomaly_analysis" in data
    assert "ai_analysis" in data


def test_scan_requires_url():

    response = client.post(
        "/scan",
        json={}
    )

    assert response.status_code == 422