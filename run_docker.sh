#!/usr/bin/env bash

# Step 1:
# Build image and add a descriptive tag
docker build -t api .

# Step 2:
# List docker images
docker image ls

# Step 3:
# Run flask app
# exposed container port (80): flask app port (8080)
docker run -p 80:8080 api

# docker system prune -a