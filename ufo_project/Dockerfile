# ufo_project/Dockerfile

# Use Miniconda3 as a base image
FROM continuumio/miniconda3:latest

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y libpoppler-dev libgdal-dev gdal-bin && \
    rm -rf /var/lib/apt/lists/*

# Copy the environment file into the container
COPY ENV.yml /app/

# Create the Conda environment
RUN conda env create -f ENV.yml

# Activate the Conda environment and set GDAL path
ENV PATH /opt/conda/envs/awm_env/bin:$PATH
ENV GDAL_LIBRARY_PATH=/opt/conda/envs/awm_env/lib/libgdal.so

# Copy the application code into the container
COPY . /app/

# Make the entrypoint script executable
RUN chmod +x /app/docker-entrypoint.sh

# Make the wait-for-it script executable
COPY wait-for-it.sh /app/wait-for-it.sh
RUN chmod +x /app/wait-for-it.sh

# Copy uWSGI configuration file
COPY uwsgi.ini /app/uwsgi.ini

# Expose port 8000 for the application
EXPOSE 8000

# Define the entrypoint
ENTRYPOINT ["./docker-entrypoint.sh"]
