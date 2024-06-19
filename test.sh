#!/usr/bin/env bash
echo "Building and starting services"
docker compose -f compose-test.yaml up -d

echo "Running tests"
docker exec -it docker-ide-hot-reload-web-testing-1 python -m unittest discover

echo "Stopping services"
docker compose -f compose-test.yaml down --rmi all -v