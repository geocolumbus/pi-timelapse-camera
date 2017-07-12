# Raspberry Pi Time Lapse Camera

## Sample Video

[![Columbus Ohio Time Lapse Video](https://img.youtube.com/vi/PmDKXX1XHno/0.jpg)](https://www.youtube.com/watch?v=PmDKXX1XHno)

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

## Running the Python Scripts

The first time you run the python camera script you will get errors about missing dependencies. That's expected - you need to install the dependencies as specified in the error messages, or from this dependencies list in the camera script:

```
from time import sleep
from picamera import PiCamera
from time import localtime, strftime
import ephem
from datetime import datetime
from dateutil import tz
import os
```

Note - we use Python3, so type ```python3``` and not ```python``` when running scripts from the command line.

For more information, see [INSTALLING PYTHON PACKAGES](https://www.raspberrypi.org/documentation/linux/software/python.md) for details on how to use ```apt-get``` or ```pip``` to install Python dependencies.
