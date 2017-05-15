#!/bin/bash

DONE_DIR=/home/pi/camera/timelapse/done

# only proceed if the done directory is empty
if find "$DONE_DIR" -mindepth 1 -print -quit | grep -q .
then
    echo "/done directory isn't empty - aborting."
else
    # loop through the files and move them to done
    FILES=/home/pi/camera/timelapse/*.jpg
    for f in $FILES
    do
        mv $f $DONE_DIR
    done
fi
