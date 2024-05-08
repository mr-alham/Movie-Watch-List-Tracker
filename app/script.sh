#!/bin/sh

sleep 3

pids=$(pgrep gunicorn)

for pid in $pids; do

	kill -TERM "$pid"

done
