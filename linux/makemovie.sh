ROOT=/home/george
DATE=`date +%Y-%m-%d`
rm "$ROOT/timelapse/movies/$DATE.mov"
/usr/local/bin/ffmpeg -r 25 -pattern_type glob -i "$ROOT/timelapse/unprocessed/*.jpg" -c:v libx264 "$ROOT/timelapse/movies/$DATE.mov"
