#!/bin/sh
trap "service cron stop; exit" INT TERM && cron && tail -f /var/log/cron.log