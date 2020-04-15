#!/bin/bash
# set -e

python3 init_py3.py
docker-compose down && docker-compose up -d --build