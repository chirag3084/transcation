#!/bin/bash

# Ensure pip is installed/updated and install dependencies
python3 -m pip install -r requirements.txt

# Run collectstatic to dump files into staticfiles_build
python3 manage.py collectstatic --noinput --clear