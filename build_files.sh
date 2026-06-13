#!/bin/bash

echo "=== Building Project ==="

# Install dependencies using pip
python3.9 -m pip install -r requirements.txt

# Collect static files
python3.9 manage.py collectstatic --noinput --clear

echo "=== Build Complete ==="