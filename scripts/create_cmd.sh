#!/bin/sh
PY=$(which python)
COMMAND="* * * * * cd /failsafe_cron && $PY main.py ${DATA_FOLDER} ${LOG_FOLDER} ${REDIS_CONNECT} ${@}"
echo "$COMMAND" | crontab -
