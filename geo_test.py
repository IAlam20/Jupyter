import os
import pandas as pd
from ctypes import cdll
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import time

geolocator = Nominatim(user_agent="myGeocoder")
location = geolocator.geocode('475 Riverside Drive, New York City, New York')

print(location)