# Incomplete. DO NOT run.
# Use Ubuntu as the base image
FROM ubuntu:22.04

# Set the working directory in the container
WORKDIR /EventPlaza

# Install system-level dependencies
RUN apt-get update && apt-get install -y \
    python3 python3-pip python3-dev python3-venv \
    default-libmysqlclient-dev build-essential pkg-config \
    git \
    && rm -rf /var/lib/apt/lists/*

# Clone the Git repository into the container
RUN git clone https://github.com/Abdorithm/EventPlaza.git .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt