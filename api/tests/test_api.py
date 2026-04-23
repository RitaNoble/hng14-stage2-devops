import pytest
import fakeredis
from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


@pytest.fixture(autouse=True)
def mock_redis(monkeypatch):
    """Fixture to mock redis for all tests."""
    fake_r = fakeredis.FakeStrictRedis(decode_responses=True)
    monkeypatch.setattr("main.r", fake_r)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_job():
    response = client.post("/jobs")
    assert response.status_code == 200
    assert "job_id" in response.json()


def test_get_job():
    # Create a job first
    res = client.post("/jobs")
    job_id = res.json()["job_id"]

    # Get the job
    response = client.get(f"/jobs/{job_id}")
    assert response.status_code == 200
    assert response.json()["job_id"] == job_id
