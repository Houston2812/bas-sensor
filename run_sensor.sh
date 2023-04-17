#!/bin/bash

echo "Running sensor"
docker-compose -f ./sensor/docker-compose.yml up --detach