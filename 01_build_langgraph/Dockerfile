FROM python:3.11-slim

# Install system dependencies for venv
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-venv \
    python3-pip \
    python3-dev \
    build-essential \
    libssl-dev \
    libffi-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Create virtual environment and install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Environment variables
ENV PYTHONUNBUFFERED=1 \
    PORT=8080

# Expose the port
EXPOSE 8080

# Start FastAPI app using uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
