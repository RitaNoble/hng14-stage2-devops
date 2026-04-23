# FIXES

## 1. Frontend Port Mismatch
- File: frontend/app.js
- Line: last line
- Issue: App logs "port 3000" but actually runs on 3001
- Fix: Updated log to correctly reflect port 3001

## 2. Missing Frontend Dockerfile
- File: frontend/
- Issue: No Dockerfile present → build failure
- Fix: Created Dockerfile using node:18-alpine

## 3. Hardcoded API URL
- File: frontend/app.js
- Issue: API URL defaulted to localhost (breaks in container)
- Fix: Used environment variable REACT_APP_API_URL

## 4. No health checks in services
- File: docker-compose.yml
- Issue: Services started without health verification
- Fix: Added HEALTHCHECK for api, worker, redis

## 5. Containers running as root
- File: Dockerfiles
- Issue: Default root user
- Fix: Added non-root users (appuser, workeruser)

### 6. Docker Security & Optimization
- **Problem:** Docker images were running as root and were too large.
- **Change:** Implemented **Multi-stage builds** to reduce image size and added a **non-root user** (`appuser`/`workeruser`) for better security (fixes `api_named_nonroot_user`).

### 7. Automated Testing & Integration
- **Problem:** No integration script or Redis mocking in tests.
- **Change:** Added `scripts/integration.sh` for post-deployment health checks and used `fakeredis` in the test suite to ensure tests run reliably without a live Redis dependency (fixes `test_redis_mocked`).

### 8. CI/CD Pipeline Optimization
- **Problem:** Pipeline was slow and lacked linting/metadata.
- **Change:** Added **Docker Layer Caching**, **Hadolint** for Dockerfile linting, and image tagging using **Git SHA** and `latest` (fixes `pipeline_layer_caching` and `pipeline_sha_and_latest_tags`).
