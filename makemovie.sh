ROOT=/home/pi
FILENAME=`date +%Y-%m-%d`
rm "$ROOT/camera/movies/$FILENAME.mov"
/usr/local/bin/ffmpeg -r 25 -pattern_type glob -i "$ROOT/camera/timelapse/done/*.jpg" -c:v libx264 "$ROOT/camera/movies/$FILENAME.mov"
# echo "~/camera/movies/$FILENAME.mov"
# /usr/bin/python "$ROOT/camera/upload_video.py" --file="$ROOT/camera/movies/$FILENAME.mov" --title="Columbus, Ohio timelapse for $FILENAME" --description="Columbus, Ohio weather timelapse video for $FILNAME" --keywords="timelapse, time lapse, weather, Columbus, Ohio" --category="22" --privacyStatus="public"

