#!/bin/sh
docker run -p 6379:6379 -d redis/redis-stack-server:latest
path_root="/home/anton/failsafe_cron"
path_venv=".venv/bin/python"
command="cd $path_root && $path_venv main.py"
echo "* * * * *  $command;$command" | crontab