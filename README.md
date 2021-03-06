# Raspberry Pi Time Lapse Camera

This project consists of a README file that explains how to set up a Raspberry Pi 3 with a V2 Camera to take timelapse photos from 1/2 hour before sunrise to 1/2 hour after sunset, and a camera python3 script and some shell scripts.

The photos are taken once every 6 seconds, and stiched together into a H264 encoded movie of about 100-200 MB in size. It takes the Pi about 1.5 hours to compress the images into videos using ffmpeg starting about 9:40 pm at the end of the day. 

## Sample Video

[![Columbus Ohio Time Lapse Video](https://img.youtube.com/vi/bHydfI2YfoE/0.jpg)](https://www.youtube.com/watch?v=bHydfI2YfoE)

## Hardware

* [Raspberry Pi 3](https://www.amazon.com/Raspberry-Model-A1-2GHz-64-bit-quad-core/dp/B01CD5VC92/ref=sr_1_3?s=pc&ie=UTF8&qid=1499880702&sr=1-3&keywords=raspberry+pi+3)
* [Rapsberry Pi Camera V2](https://www.amazon.com/Raspberry-Pi-Camera-Module-Megapixel/dp/B01ER2SKFS/ref=sr_1_3?s=electronics&ie=UTF8&qid=1499880820&sr=1-3&keywords=raspberry+pi+3+camera)
* [Raspberry Pi power supply](https://www.amazon.com/CanaKit-Raspberry-Supply-Adapter-Charger/dp/B00MARDJZ4/ref=sr_1_1?s=electronics&ie=UTF8&qid=1499880799&sr=1-1-spons&keywords=raspberry+pi+3+power+supply&psc=1)
* [SD Card](https://www.amazon.com/SanDisk-microSDHC-Standard-Packaging-SDSQUNC-032G-GN6MA/dp/B010Q57T02/ref=pd_bxgy_147_img_2?_encoding=UTF8&psc=1&refRID=N2HGSMWD8V6H4245YZ9P)

## Configure the Pi

### Basic Configuration Information

This is hardly complete, but it is basic info to get a Raspberry Pi up and running as headless server on a home WIFI network.

* [Download Raspbian](https://www.raspberrypi.org/downloads/)
* [Use Apple Pi Baker to get Raspbian onto an SD Card](https://www.tweaking4all.com/hardware/raspberry-pi/macosx-apple-pi-baker/)
* Boot up the Pi and update everything ```sudo apt-get update && sudo apt-get upgrade```
* Set the hostname ```sudo nano /etc/hostname```
* Configure the pi from the command line ```sudo raspi-config``` - you can set the root user, etc.
* Install git ```sudo apt-get install git```
* [How to Setup Wi-Fi and Bluetooth on the Raspberry Pi 3](http://www.makeuseof.com/tag/setup-wi-fi-bluetooth-raspberry-pi-3/)
* [“Americanizing” the Raspberry Pi](http://rohankapoor.com/2012/04/americanizing-the-raspberry-pi/)

#### Install SSH to the Pi

```
mkdir ~/.ssh
cd ~/.ssh
chmod 700 ~/.ssh
wget https://dl.dropboxusercontent.com/u/somenumber/authorized_keys  <- stick your key up on Dropbox!
chmod 600 ~/.ssh/authorized_keys
sudo raspi-config   <— turn on the ssh
```

### Install the Camera

The camera can be controlled by running python3 scripts.

```sudo apt-get install python3-picamera```

Turn the camera on from rasp-config

```sudo raspi-config```

see [Raspberry Pi Basic Camera Recipes](http://picamera.readthedocs.io/en/release-1.13/recipes1.html) for details on how to write python code for the camera.

### Install ffmpeg

ffmpeg converts the individual timelapse photos into a compressed, high definition video.

build and install x264
```
git clone --depth 1 git://git.videolan.org/x264
cd x264
./configure --host=arm-unknown-linux-gnueabi --enable-static --disable-opencl
make -j 4
sudo make install
``` 
build and make ffmpeg
```
git clone --depth=1 git://source.ffmpeg.org/ffmpeg.git
cd ffmpeg
```
Note - set architecture to ```armhf``` for Pi3 (hardware float) vs. ```armel``` for Pi2 (software float).
```
./configure --arch=armhf --target-os=linux --enable-gpl --enable-libx264 --enable-nonfree
make -j 4
sudo make install
```

see [ffmpeg on raspbian / Raspberry Pi](http://hannes.enjoys.it/blog/2016/03/ffmpeg-on-raspbian-raspberry-pi/
) for more details on ffmpeg.

To execute ffmpeg, use the makemovie.sh script.

```
# Takes files from the timelapse/done folder and stiches them into a movie in the movies folder. 
ROOT=/home/pi
FILENAME=`date +%Y-%m-%d`
rm "$ROOT/camera/movies/$FILENAME.mov"
/usr/local/bin/ffmpeg -r 25 -pattern_type glob -i "$ROOT/pi-timelapse-camera/timelapse/done/*.jpg" -c:v libx264 "$ROOT/pi-timelapse-camera/movies/$FILENAME.mov"
```

## Running the Python Scripts

```git clone https://github.com/geocolumbus/pi-timelapse-camera.git```

```cd pi-timelapse-camera```

Create these folders:

```
pi-timelapse-camera
  |-timelapse
  |  |-done
  |-movies
```

Run the script ```python3 cam.py``` and images will start accumulating in the timelapse folder.

The first time you run the python camera script you will get errors about missing dependencies. That's expected - you need to install the dependencies as specified in the error messages, or from this dependencies list in the camera script. See [INSTALLING PYTHON PACKAGES](https://www.raspberrypi.org/documentation/linux/software/python.md) for details on how to use ```apt-get``` or ```pip``` to install Python dependencies.

```
from time import sleep
from picamera import PiCamera
from time import localtime, strftime
import ephem
from datetime import datetime
from dateutil import tz
import os
```

A sample crontab is supplied to tie the system together. The python script adds a new image to the timelapse folder every 6 seconds. Every so often, those images are moved to the timelapse/done folder. At 9:40pm, a makemovie.sh script converts the images in the timelapse/done folder into a H264 encoded move in the movies folder.
