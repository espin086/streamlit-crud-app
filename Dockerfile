# Dockerfile, Image, Container

# Base Image gets pulled from Docker Hub
FROM python:3.8

# Set the working directory in the Docker image
WORKDIR /streamlit-crud-app/

# Copy the files from the host to the working directory in the Docker image
COPY . .

# Install the dependencies
RUN pip3 install -r ./requirements.txt

# Expose the port
EXPOSE 8501

# Command to run the application
CMD ["streamlit", "run", "./app.py"]



