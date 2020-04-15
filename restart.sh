#!/bin/bash
# set -e

python3 initialize.py
docker-compose down && docker-compose up -d --build
