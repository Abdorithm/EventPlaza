# Incomplete. DO NOT run.
# Use Ubuntu as the base image
FROM ubuntu:22.04

# Set the working directory in the container
WORKDIR /EventPlaza

# Install system-level dependencies
RUN apt-get update && apt-get install -y mysql-server \
    python3 python3-pip python3-dev \
    default-libmysqlclient-dev build-essential pkg-config \
    git \
    && rm -rf /var/lib/apt/lists/*

# Start MySQL
RUN service mysql start

# Clone the Git repository into the container
RUN git clone https://github.com/Abdorithm/EventPlaza.git .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Here we should run the setup_mysql_dev.sql
RUN mysql < setup_mysql_dev.sql

# Expose the port on which your Flask app runs
EXPOSE 5000

# Define the command to run your Flask app
CMD ["python3", "-m", "app"]