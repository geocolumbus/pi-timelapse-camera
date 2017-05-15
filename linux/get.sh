#!/bin/bash

ROOT=/home/george
PIDFILE=~/timelapse/PIDFILE
if [ ! -f $PIDFILE ]
then
  echo $$ > $ROOT/timelapse/PIDFILE
  cd $ROOT/timelapse/unprocessed
  /usr/bin/sftp -b $ROOT/timelapse/script.sftp pi@192.168.1.68
  rm $ROOT/timelapse/PIDFILE
fi
