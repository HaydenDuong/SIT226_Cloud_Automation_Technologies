# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
# We'll create a requirements.txt file next for best practice
COPY deployment/requirements.txt /app/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the local directory contents into the container at /app
COPY ./app.py /app/app.py
COPY ./templates /app/templates/
COPY ./static /app/static/

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable (optional, can be set at runtime too)
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0

# Run app.py when the container launches
CMD ["flask", "run"] 
# Alternatively, if you prefer gunicorn or another WSGI server for later:
# CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"] 
# For now, sticking to flask run as per basic setup, K8s will manage replicas. 