# Use an official Python runtime as a parent image
FROM python:3.11.5-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable for Flask to run in production mode
ENV FLASK_ENV=production

# Ensure the directories are writable by the Flask application
RUN mkdir -p /app/resume_folder && \
    mkdir -p /app/job_folder && \
    chmod -R 755 /app/resume_folder /app/job_folder

# Run the application using the module run syntax
CMD ["python", "-m", "app.routes"]
