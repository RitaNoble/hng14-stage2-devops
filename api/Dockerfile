# Stage 1: Build
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt
COPY . .

# Stage 2: Production
FROM python:3.11-slim
RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*
RUN useradd -m appuser
WORKDIR /app

# Copy from builder
COPY --from=builder /root/.local /home/appuser/.local
COPY --from=builder /app /app

# Set permissions
RUN chown -R appuser:appuser /app
ENV PATH=/home/appuser/.local/bin:$PATH
USER appuser

# Healthcheck
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/health || exit 1

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
