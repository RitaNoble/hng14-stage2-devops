#hng14-stage2-devops

📦 DevOps Stage 2 – Microservices Job Processing System
📌 Overview

This project is a containerized microservices job processing system built as part of the HNG Stage 2 DevOps assessment.

It consists of three core services:

Frontend (Node.js) – Accepts job submissions and displays job status
API (FastAPI - Python) – Handles job creation and status tracking
Worker (Python) – Processes queued jobs asynchronously
Redis – Acts as the shared job queue

All services are containerized using Docker and orchestrated with Docker Compose, and deployed through a CI/CD pipeline using GitHub Actions.

🏗️ System Architecture
Frontend → API → Redis Queue → Worker → API → Frontend
Flow Explanation:
User submits a job via the frontend
Frontend sends request to API
API stores job in Redis queue
Worker picks job from Redis and processes it
Worker updates job status
API returns updated status to frontend/client
⚙️ Prerequisites

Ensure the following are installed:

Docker (>= 20+)
Docker Compose
Git
curl
jq
🚀 How to Run the Application
1. Clone the repository
git clone https://github.com/<your-username>/hng14-stage2-devops.git
cd hng14-stage2-devops
2. Start all services
docker compose up -d --build
3. Verify services are running
docker ps

Expected containers:

api
worker
redis
4. Test API manually

Create a job:

curl -X POST http://localhost:8000/jobs

Response:

{
  "job_id": "xxxx-xxxx"
}

Check job status:

curl http://localhost:8000/jobs/<job_id>

Expected output:

{
  "job_id": "...",
  "status": "completed"
}
🧪 Running Tests
API Unit Tests
pytest api/tests -v

Tests include:

Job creation
Job status retrieval
Redis mocking validation
🔐 Environment Variables

The system uses the following environment variables:

API / Worker
REDIS_HOST=redis
REDIS_PORT=6379
🐳 Docker Services
API Service
Built from ./api
Exposes port 8000
Handles job lifecycle
Worker Service
Built from ./worker
Consumes jobs from Redis queue
Redis Service
Internal service only
Not exposed externally
🔄 CI/CD Pipeline

The GitHub Actions pipeline runs in the following order:

lint → test → build → security scan → integration test → deploy
Pipeline Stages
1. Lint
Python: flake8
Ensures code style consistency
2. Test
Pytest for API
Redis is mocked
3. Build
Builds Docker images for API and Worker
4. Security Scan
Trivy scans all images
Fails on CRITICAL vulnerabilities
Uploads SARIF reports as artifacts
5. Integration Test
Spins up full stack using Docker Compose
Submits a job via API
Polls until completion
Validates final job status
6. Deploy
Runs only on main
Performs rolling update with health checks
📊 Success Criteria

A successful run should show:

All containers running without errors
Job successfully created
Worker processes job
Final status = completed
Pipeline passes all stages
🧾 Documentation
README.md → System setup and usage guide
FIXES.md → List of all bugs found and fixed during development
.env.example → Required environment variables template
⚠️ Important Notes
.env files must NOT be committed
All services must communicate via Docker internal network
Redis must NOT be exposed externally
All services must run as non-root users inside containers
👩‍💻 Author

Built as part of HNG Stage 2 DevOps Track submission.
