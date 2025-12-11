#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files (CSS/Images)
python manage.py collectstatic --no-input

# Run migrations (Update Production DB)
python manage.py migrate