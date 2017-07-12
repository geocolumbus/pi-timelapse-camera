ROOT=/home/pi
FILENAME=`date +%Y-%m-%d`
rm "$ROOT/camera/movies/$FILENAME.mov"
/usr/local/bin/ffmpeg -r 25 -pattern_type glob -i "$ROOT/camera/timelapse/done/*.jpg" -c:v libx264 "$ROOT/camera/movies/$FILENAME.mov"

