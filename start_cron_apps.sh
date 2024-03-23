#!/bin/sh
CONTAINER_ID=$(docker ps -a -q -f name=redis)
PATH_ROOT="~/failsafe_cron"
PATH_VENV=".venv/bin/python"
COMMAND="* * * * * cd $PATH_ROOT && $PATH_VENV main.py"

if [ -z "$CONTAINER_ID" ]; then
    docker run -p 6379:6379 --name redis -d redis/redis-stack-server:latest
else
    docker start $CONTAINER_ID
fi

(crontab -l &> /dev/null && (crontab -l ; echo "$COMMAND")) || echo "$COMMAND" | crontab - 
(crontab -l ; echo "$COMMAND") | crontab -