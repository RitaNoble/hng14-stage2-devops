import sys
import os
from unittest.mock import MagicMock, patch

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


@patch("main.r")
def test_health(mock_redis):
    response = client.get("/health")
    assert response.status_code == 200


@patch("main.r")
def test_create_job(mock_redis):
    mock_redis.lpush = MagicMock()
    mock_redis.set = MagicMock()

    response = client.post("/jobs")

    assert response.status_code in [200, 201]
    assert "job_id" in response.json()


@patch("main.r")
def test_get_job(mock_redis):
    mock_redis.get.return_value = b"queued"

    create = client.post("/jobs")
    job_id = create.json().get("job_id")

    response = client.get(f"/jobs/{job_id}")

    assert response.status_code == 200
    assert response.json()["job_id"] == job_id
