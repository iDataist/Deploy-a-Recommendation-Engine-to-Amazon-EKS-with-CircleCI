#!/usr/bin/env bash

# This tags and uploads an image to Docker Hub

# Step 1:
# This is your Docker ID/path
dockerpath=hwdgrmy/api

# Step 2
# Run the Docker Hub container with kubernetes
kubectl run apipod --image=$dockerpath --port=80

# Step 3:
# List kubernetes pods
kubectl get pods

# Step 4:
# Forward the container port to a host
# exposed container port (80): flask app port (5000)
kubectl port-forward --address 0.0.0.0 apipod 80:5000

# kubectl delete pod <POD NAME>
# kubectl logs <POD NAME>
