# Raspberry Pi Time Lapse Camera

## Sample Video

[![Columbus Ohio Time Lapse Video](https://img.youtube.com/vi/PmDKXX1XHno/0.jpg)](https://www.youtube.com/watch?v=PmDKXX1XHno)

# pi-timelapse-camera
Raspberry Pi timelapse camera files

TODO - detail RPi setup to create a timelapse camera

## Configure the Pi

### Basic Configuration Information

* [Download Raspbian](https://www.raspberrypi.org/downloads/)
* [Use Apple Pi Baker to get Raspbian onto an SD Card](https://www.tweaking4all.com/hardware/raspberry-pi/macosx-apple-pi-baker/)
* Boot up the Pi and update everything ```sudo apt-get update && sudo apt-get upgrade```
* Configure the pi from the command line ```sudo raspi-config```
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
