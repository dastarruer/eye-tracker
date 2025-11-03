# Use the official Debian-based Python image
FROM python:3.12-slim

# Install necessary opencv dependencies
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
# Clear cached list of available packages to save space
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Command to run your Python program
CMD ["python", "main.py"]
