#!/bin/bash
set -e
echo "🚀 Running Integration Health Check..."
# Try to hit the health endpoint
if curl -s http://localhost:8000/health | grep -q "ok"; then
  echo "✅ API is Healthy!"
  exit 0
else
  echo "❌ API Health Check Failed"
  exit 1
fi
