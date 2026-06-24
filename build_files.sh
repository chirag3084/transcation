#!/bin/bash

echo "=== BUILD START ==="

# Install requirements safely into the local container environment
python3 -m pip install --upgrade pip
uv install -r requirements.txt


# Run Django collectstatic
python3 manage.py collectstatic --noinput --clear

echo "=== BUILD END ==="
