#!/bin/bash

if [ `ps -ax | grep '/home/pi/pi-timelapse-camera/cam.py' | grep -v 'sudo' | grep -v 'grep' | wc -l` = "1" ]; then
   echo "[ALREADY RUNNING]"
   echo `ps -ax | grep '/home/pi/pi-timelapse-camera/cam.py' | grep -v grep`
else
   echo "[STARTING]"
   /usr/bin/python3 /home/pi/pi-timelapse-camera/cam.py &
   echo `ps -ax | grep '/home/pi/pi-timelapse-camera/cam.py' | grep -v grep`
fi
