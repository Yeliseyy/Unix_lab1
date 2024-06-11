#!/bin/bash

# Build the Docker image
docker build -t my_flask_app .

# Run the Docker container
docker run -d -p 5000:5000 --name my_flask_app_container -v $(pwd)/data:/app/data my_flask_app
