from time import sleep
from picamera import PiCamera
from time import localtime, strftime
import ephem
from datetime import datetime
from dateutil import tz
import os

def isDay():
   user = ephem.Observer()
   user_sunset = ephem.Observer()
   user_sunrise = ephem.Observer()

   user.lat = '40.0931'      # Worthington, OH
   user_sunset.lat = user.lat
   user_sunrise.lat = user.lat

   user.lon = '-83.0180'         # Worthington, OH
   user_sunset.lon = '-91.0180'  # A half hour later than Worthington, OH, 1 hr = 15 degrees
   user_sunrise.lon = '-75.0180' # A half hour earlier than Worthington, OH

   user.elevation = 274      # Worthingtonm OH (meters)
   user.temp = 20            # current air temperature gathered manually
   user.pressure = 1019.5    # current air pressure gathered manually

   user_sunset.elevation = user.elevation
   user_sunrise.elevation = user.elevation

   user_sunset.temp = user.temp
   user_sunrise.temp = user.temp

   user_sunset.pressure = user.pressure
   user_sunrise.pressure = user.pressure

   next_sunrise_datetime = user_sunrise.next_rising(ephem.Sun()).datetime()
   next_sunset_datetime = user_sunset.next_setting(ephem.Sun()).datetime()

   from_zone = tz.gettz('UTC')
   to_zone = tz.gettz('America/New_York')

   local_sunrise = next_sunrise_datetime.replace(tzinfo=from_zone).astimezone(to_zone)
   local_sunset = next_sunset_datetime.replace(tzinfo=from_zone).astimezone(to_zone)

   it_is_day = local_sunset < local_sunrise
   it_is_night = local_sunrise < local_sunset

   return it_is_day

def captureImage(camera):
    camera.start_preview()
    # Give camera time to focus and adjust to light levels
    sleep(4)
    filename = "/home/pi/camera/timelapse/" + strftime("%Y-%m-%d_%H-%M-%S", localtime())+".jpg"
    camera.capture(filename) 
    os.system("convert -pointsize 60 -fill yellow -draw \"text 50,1040 \\\"`date '+%Y-%m-%d %H:%M'`\\\"\" "+filename+" "+filename)

# Initialize camera
camera = PiCamera()
camera.resolution = (1920, 1080)

# Main loop
while 1==1:
    if isDay() == True:
        captureImage(camera)
    sleep(1);

# Never reaches this point (TODO)
# camera.close()
