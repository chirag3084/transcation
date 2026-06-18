#!/bin/bash

# Force pip to install packages globally in the build container
python3 -m pip install -r requirements.txt --break-system-packages

# Run collectstatic
python3 manage.py collectstatic --noinput --clear