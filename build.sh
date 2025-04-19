#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
python -m pip install --upgrade pip
pip install -r req.txt

# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate

# Create superuser (if not exists)
python manage.py shell <<EOF
from django.contrib.auth import get_user_model

User = get_user_model()
if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("admin", "admin@example.com", "1234")
    print("Superuser created!")
else:
    print("Superuser already exists.")
EOF
