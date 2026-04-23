#!/bin/bash
set -e
echo "Running Integration Test..."
# Check API health
URL="http://localhost:8000/health"
STATUS=$(curl -s -o /dev/null -w "%{http_code}" $URL)

if [ "$STATUS" -eq 200 ]; then
  echo "Integration Test Passed"
  exit 0
else
  echo "Integration Test Failed with status $STATUS"
  exit 1
fi
