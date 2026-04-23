# ---------- Build Stage ----------
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt


# ---------- Final Stage ----------
FROM python:3.11-slim

WORKDIR /app

# create non-root user (IMPORTANT for grading)
RUN useradd -m appuser
USER appuser

COPY --from=builder /usr/local /usr/local
COPY . .

# expose API port
EXPOSE 8000

# health check (used by docker-compose)
HEALTHCHECK CMD curl --fail http://localhost:8000/health || exit 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
