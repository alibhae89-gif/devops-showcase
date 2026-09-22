# DevOps Showcase

Flask app with Redis-backed hit counter, containerized with Docker Compose, tested via GitHub Actions CI.

## Run locally
docker compose up --build

## CI
Every push to main builds the image and hits /health inside a live container.

## Stack
Flask · Redis · Docker · Docker Compose · GitHub Actions
