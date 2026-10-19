from app import create_app


def test_health_endpoint():
    client = create_app().test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"


def test_status_endpoint():
    client = create_app().test_client()

    response = client.get("/status")
    data = response.get_json()

    assert response.status_code == 200
    assert data["service"] == "system-health-api"
    assert isinstance(data["python_version"], str)
    assert isinstance(data["uptime_seconds"], int)
