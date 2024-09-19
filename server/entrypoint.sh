#!/bin/sh


# Apply database migrations
echo "Applying migrations..."
python manage.py migrate --no-input

# Start the server
echo "Starting server..."
exec python manage.py runserver 0.0.0.0:8000
