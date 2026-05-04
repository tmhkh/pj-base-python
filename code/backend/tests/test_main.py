from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_echo_message():
    test_payload = {"text": "Hello Pytest!"}
    response = client.post("/api/v1/messages/echo", json=test_payload)
    
    assert response.status_code == 200
    data = response.json()
    assert "echo" in data
    assert data["echo"] == "Hello Pytest!"