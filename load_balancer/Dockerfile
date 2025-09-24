# Base image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn

# Copy project
COPY . .

# Collect static files (if using static)
RUN python manage.py collectstatic --noinput

# Run gunicorn
CMD ["gunicorn", "load_balancer.wsgi:application", "--bind", "0.0.0.0:8000"]
