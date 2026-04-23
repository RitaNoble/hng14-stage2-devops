# =========================
# 1. Build Stage
# =========================
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# =========================
# 2. Production Stage
# =========================
FROM python:3.11-slim

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

RUN useradd -m appuser

WORKDIR /app

COPY --from=builder /usr/local /usr/local
COPY --from=builder /app /app

RUN chown -R appuser:appuser /app

USER appuser

EXPOSE 8000

# IMPORTANT FIX FOR YOUR HEALTHCHECK ISSUE
HEALTHCHECK --interval=10s --timeout=5s --start-period=20s --retries=5 \
  CMD curl -fs http://localhost:8000/health || exit 1

CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port 8000"]
