# =========================
# 1. Build Stage
# =========================
FROM python:3.11-slim AS builder

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Copy source code
COPY . .

# =========================
# 2. Production Stage
# =========================
FROM python:3.11-slim

WORKDIR /app

COPY --from=builder /install /usr/local
COPY --from=builder /app /app

# Create user + fix permissions in ONE layer
RUN useradd -m workeruser && \
    chown -R workeruser:workeruser /app

USER workeruser

HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
  CMD python -c "import redis; print('ok')" || exit 1

CMD ["python", "-u", "worker.py"]
