#!/bin/bash

# Define the Docker image/app name
APP_NAME="llm-agent-learning"

# Function to build the Docker image
build_image() {
    echo "Building Docker image..."
    docker build -t $APP_NAME .
    echo "Build complete."
}

# Function to run the Docker container with local mounting
run_container() {
    echo "Running Docker container..."
    docker run --network="host" -it -p 8000:8000 -v $(pwd):/app $APP_NAME
    echo "Container is running."
}

# Function to interact with a running Docker container
interact_container() {
    echo "Listing running containers..."
    docker ps -a
    read -p "Enter the container ID or name to interact with: " container_id
    docker exec -it $container_id /bin/bash
}

# Handling command-line arguments
case "$1" in
    build)
        build_image
        ;;
    run)
        run_container
        ;;
    interact)
        interact_container
        ;;
    *)
        echo "Usage: $0 {build|run|interact}"
        exit 1
        ;;
esac

exit 0
