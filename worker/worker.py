import redis
import time
import os

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))

print("Worker starting...")

r = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True
)

while True:
    print("Waiting for job...")

    job = r.brpop("job", timeout=5)

    if job:
        _, job_id = job
        print(f"Processing job: {job_id}")

        time.sleep(2)

        r.hset(f"job:{job_id}", "status", "completed")

        print(f"Done job: {job_id}")
