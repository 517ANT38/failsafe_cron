#!/bin/sh
docker run -p 6379:6379 -d redis/redis-stack-server:latest
echo "* * * * * $USER $(pwd)/run.sh; $USER $(pwd)/run.sh" > apps
crontab apps