#!/bin/sh

COMMAND="* * * * * root python /failsafe_cron/main.py ${DATA_FOLDER} ${LOG_FOLDER} ${REDIS_CONNECT} ${@}"
(echo "$COMMAND";echo "$COMMAND") | crontab -
