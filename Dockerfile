# Base image
FROM python:3.8


RUN pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cpu
# Install Poppler dependencies
RUN apt-get update && apt-get install -y \
    libpoppler-cpp-dev \
    pkg-config \
    python3-dev \
    python3-pip \
    poppler-utils
    
# Copy application code
COPY main.py /app/main.py
COPY saved_models/ /app/saved_models/
COPY src/ /app/src/

# Set working directory
WORKDIR /app

# Install Python dependencies
COPY requirements_linux.txt /app/requirements_linux.txt
RUN pip install --no-cache-dir -r /app/requirements_linux.txt

ENV PORT=8000

# Expose port
EXPOSE 8000

# Define the startup command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]