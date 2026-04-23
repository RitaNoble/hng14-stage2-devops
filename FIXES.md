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

