#!/bin/sh

sleep 3

pids=$(pgrep -f "app.py")

for pid in $pids; do
    kill -9 $pid
done
