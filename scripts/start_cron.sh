#!/bin/sh

COMMAND="* * * * * /usr/bin/python /failsafe_cron/main.py"

(crontab -l &> /dev/null && (crontab -l ; echo "$COMMAND")) || echo "$COMMAND" | crontab - 
(crontab -l ; echo "$COMMAND") | crontab -