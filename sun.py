from time import sleep
from picamera import PiCamera
from time import localtime, strftime
import ephem
from datetime import datetime
from dateutil import tz

def isDay():
   user = ephem.Observer()
   user_sunset = ephem.Observer()
   user_sunrise = ephem.Observer()

   user.lat = '40.0931'      # Worthington, OH
   user_sunset.lat = user.lat
   user_sunrise.lat = user.lat

   user.lon = '-83.0180'     # Worthington, OH
   user_sunset.lon = '-90.0180'
   user_sunrise.lon = '-76.0180'

   user.elevation = 274      # See wikipedia.org/Oldenburg
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

   print(local_sunrise)
   print(local_sunset)

   return it_is_day

isDay()
