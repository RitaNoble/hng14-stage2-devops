import sys
import os

# Fix import path so pytest can find main.py
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_create_job():
    response = client.post("/jobs")
    assert response.status_code == 200
    assert "job_id" in response.json()


def test_get_job():
    job = client.post("/jobs").json()["job_id"]
    response = client.get(f"/jobs/{job}")
    assert response.status_code == 200
    assert response.json()["job_id"] == job
