# Raspberry Pi Time Lapse Camera

## Sample Video

[![Columbus Ohio Time Lapse Video](https://img.youtube.com/vi/PmDKXX1XHno/0.jpg)](https://www.youtube.com/watch?v=PmDKXX1XHno)

# pi-timelapse-camera
Raspberry Pi timelapse camera files

TODO - detail RPi setup to create a timelapse camera

## Configure the Pi

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
Note - use armhf for hardware float (Pi3) vs. armel for software float
```./configure --arch=armhf --target-os=linux --enable-gpl --enable-libx264 --enable-nonfree
make -j 4
sudo make install
```
