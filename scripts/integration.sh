#!/bin/bash
set -e
echo "🚀 Running Integration Health Check..."
HEALTH=$(curl -s http://localhost:8000/health)
if [[ $HEALTH == *"ok"* ]]; then
  echo "✅ API is Healthy!"
  exit 0
else
  echo "❌ API Health Check Failed: $HEALTH"
  exit 1
fi
