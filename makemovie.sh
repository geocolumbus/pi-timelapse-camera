# Takes files from the timelapse/done folder and stiches them into a movie in the movies folder. 
ROOT=/home/pi
FILENAME=`date +%Y-%m-%d`
rm "$ROOT/camera/movies/$FILENAME.mov"
/usr/local/bin/ffmpeg -r 25 -pattern_type glob -i "$ROOT/pi-timelapse-camera/timelapse/done/*.jpg" -c:v libx264 "$ROOT/pi-timelapse-camera/movies/$FILENAME.mov"

