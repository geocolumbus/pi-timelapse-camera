#!/bin/bash

if [ `ps -ax | grep '/home/pi/pi-timelapse-camera/cam.py' | grep -v grep | grep -v sudo | wc -l` = "1" ]; then
   echo "[RUNNING]"
   echo  `ps -ax | grep '/home/pi/pi-timelapse-camera/cam.py' | grep -v grep`
else
   echo "[PROCESS NOT FOUND]"
fi

