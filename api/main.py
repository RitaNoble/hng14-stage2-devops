from fastapi import FastAPI
import redis
import os
import uuid

# Create FastAPI app FIRST (this was your error)
app = FastAPI()

# Environment variables (works for Docker + local pytest)
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379") or "6379")

# Redis connection
r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)


# Health check endpoint
@app.get("/health")
def health():
    return {"status": "ok"}


# Create job
@app.post("/jobs")
def create_job():
    job_id = str(uuid.uuid4())
    r.lpush("jobs", job_id)
    r.set(job_id, "queued")
    return {"job_id": job_id}


# Get job status
@app.get("/jobs/{job_id}")
def get_job(job_id: str):
    status = r.get(job_id)

    if not status:
        return {"error": "Job not found"}

    return {
        "job_id": job_id,
        "status": status
    }
