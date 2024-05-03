# Incomplete. DO NOT run.
# Use Ubuntu 22.04 as the base image
FROM ubuntu:22.04

# Set the working directory in the container
WORKDIR /app

# Install system-level dependencies
RUN apt-get update && apt-get install -y \
    python3 python3-pip python3-dev \
    default-libmysqlclient-dev build-essential pkg-config \
    mysql-client \
    git \
    && rm -rf /var/lib/apt/lists/*

# Clone the Git repository into the container
RUN git clone https://github.com/Abdorithm/EventPlaza.git .

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Here we should run the setup_mysql_dev.sql
# We need to make sure that the database engine works

# Expose the port on which your Flask app runs
EXPOSE 5000

# Define the command to run your Flask app
CMD ["python3", "-m", "app"]
