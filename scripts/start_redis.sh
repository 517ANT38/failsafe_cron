#!/bin/sh
GD=docker
GU=$(groups "$USER" | grep -o -w "\b$GD\b")

if [ "$GD" = "$GU" ]; then
    CONTAINER_ID=$(docker ps -a -q -f name=redis)
    if [ -z "$CONTAINER_ID" ]; then
        docker run -p 6379:6379 --name redis -d redis/redis-stack-server:latest > /dev/null
    else
        docker start $CONTAINER_ID > /dev/null
    fi
else
    echo "User $USER is not a member of the Docker group."
    exit 1
fi