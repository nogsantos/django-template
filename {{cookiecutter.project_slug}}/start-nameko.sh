#!/bin/sh

echo "Starting nameko server"
pipenv run nameko run --config config.yaml core.services
