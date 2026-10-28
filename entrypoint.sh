#!/bin/sh

set -e

echo "Running database migrations..."


echo "Starting FastAPI..."

exec uvicorn app.main:app --host 0.0.0.0 --port 8005 --reload