# Dockerfile for Django app
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project
COPY . /app/

COPY entrypoint.sh /app/

RUN chmod +x /app/entrypoint.sh

EXPOSE 8000

# Set the entrypoint script as the container entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]

# Run migrations and start the server
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
