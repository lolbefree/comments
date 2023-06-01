FROM python:3.9-slim-buster

# Install Python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r /app/requirements.txt

# Copy project files
COPY . /app/
WORKDIR /app/

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Collect static files

# Expose port 8000 for Gunicorn
EXPOSE 8000

# Start Gunicorn
CMD ["gunicorn", "comments.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
