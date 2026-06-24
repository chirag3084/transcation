#!/bin/bash

echo "=== BUILD START ==="

# Install requirements safely into the local container environment
python3 -m pip install --upgrade pip
pip install -r requirements.txt --break-system-packages


# Run Django collectstatic
python3 manage.py collectstatic --noinput --clear

echo "=== BUILD END ==="
