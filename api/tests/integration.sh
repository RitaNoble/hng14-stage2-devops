#!/bin/bash
set -e

timeout 30s bash -c '
until curl -f http://localhost:8000/health; do
  sleep 2
done
'

curl -X POST http://localhost:8000/jobs
