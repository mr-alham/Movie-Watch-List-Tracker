#!/bin/sh

sleep 3

# pids=$(ps aux|grep 'gunicorn'|cut -d ' ' -f 1-10 |grep -Eo '[0-9]+')
pids=$(pgrep gunicorn)

for pid in $pids; do
     kill -TERM "$pid"
done
