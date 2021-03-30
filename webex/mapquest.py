import requests, urllib.parse
from datetime import datetime
import json

def mapping(text):
    location = text[1:]
    url = "http://www.mapquestapi.com/geocoding/v1/address?"
    key = "CVHxRa9OD4bZHjgeEpsq51fXfX9YVQQX"
    url_map = url + urllib.parse.urlencode({"key":key, "location":location})
    json_data = requests.get(url_map).json()
    lat = json_data["results"][0]["locations"][0]["latLng"]["lat"]
    lon = json_data["results"][0]["locations"][0]["latLng"]["lng"]
    return [lat, lon]

def iss(location):
    lat = location[0]
    lon = location[1]
    url = "http://api.open-notify.org/iss-pass.json?"
    url_iss = url + urllib.parse.urlencode({"lat":lat, "lon":lon})
    json_data = requests.get(url_iss).json()
    duration = json_data["response"][0]["duration"]
    timestamp = json_data["response"][0]["risetime"]
    date_time = datetime.fromtimestamp(timestamp)
    return [duration, date_time]