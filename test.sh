#!/usr/bin/env bash
echo "Building and starting services"
docker compose -f compose-test.yaml up -d

echo "Running tests"
docker exec -it $(docker ps --filter "name=web-testing" --format "{{.ID}}") python -m unittest discover

echo "Stopping services"
docker compose -f compose-test.yaml down --rmi all -v