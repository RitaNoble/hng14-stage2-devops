# Stage 1: Build
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Stage 2: Production
FROM python:3.11-slim
# Install curl for healthcheck
RUN apt-get update && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN useradd -m appuser
WORKDIR /app

# Copy from builder
COPY --from=builder /usr/local /usr/local
COPY --from=builder /app /app
RUN chown -R appuser:appuser /app

USER appuser
EXPOSE 8000

# Single, clean Healthcheck
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3
