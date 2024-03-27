#!/bin/sh

COMMAND="* * * * * python /failsafe_cron/main.py ${DATA_FOLDER} ${LOG_FOLDER} ${REDIS_CONNECT} ${@}"
echo "$COMMAND" | crontab -
