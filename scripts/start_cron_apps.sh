#!/bin/sh
PATH_ROOT="~/failsafe_cron"
PATH_VENV=".venv/bin/python"
COMMAND="* * * * * cd $PATH_ROOT && $PATH_VENV main.py"

(crontab -l &> /dev/null && (crontab -l ; echo "$COMMAND")) || echo "$COMMAND" | crontab - 
(crontab -l ; echo "$COMMAND") | crontab -