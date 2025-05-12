# Use an official Python image as base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Expose a port if needed (adjust if you're using FastAPI/Flask/etc.)
EXPOSE 8000

# Run the application
CMD ["python", "-u", "main.py"]