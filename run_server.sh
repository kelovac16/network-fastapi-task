#!/usr/bin/env bash
echo Starting...
exec uvicorn app:app --host 0.0.0.0 --port 8080 --log-level info