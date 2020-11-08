from .api import API
from .place import Place
from .coordinate import Coordinate
import requests
import re
class Google_Maps(API):

    def get_travel_time(self, origin, dest, mode):
        """
        Returns the number minutes between `origin` and `dest` when travelling by `mode`
        """

        # define Endpoint
        distance_api_url = "https://maps.googleapis.com/maps/api/distancematrix/json"
        # Define Request Parameters
        payload = {'unit':'metric',
                   'origins': origin,
                   'destinations': dest,
                   'mode': mode,
                   'key': self._api_key}

        # GET Request
        json_response = requests.get(distance_api_url, params=payload).json()
        print("GOOGLE MAPS: ", json_response)
        duration = 0
        # Try to Parse String, otherwise return Error
        try:
            dur_str = json_response['rows'][0]['elements'][0]['duration']['text']
            print(dur_str)

            # Get mins
            m = re.search(r'(\d*) mins?', dur_str)
            if(m != None):
                duration += int((m.group(1)))

            # Get hours
            h = re.search(r'(\d*) hours?', dur_str)
            if(h != None):
                duration += int((h.group(1)))

            # Get Days
            d = re.search(r'(\d*) days?', dur_str)
            if(d != None):
                duration += int((d.group(1)))

        except:
            return -1

        return duration

    def get_geocode(self, address):
        """
        Returns the Coordinate (lat, lng) of `address`
        """

        # Define endpoint
        geocode_api_url = "https://maps.googleapis.com/maps/api/geocode/json"

        # Define Request Parameters
        payload = {'address':address, 'key':self._api_key }

        # Get JSON Response
        json_response = requests.get(geocode_api_url, params=payload).json()
        print("GEO CODE: ", json_response)
        # Try to Parse the String, otherwise return Error
        try:
            lat_str = json_response['results'][0]['geometry']['location']['lat']
            lng_str = json_response['results'][0]['geometry']['location']['lng']


        except:
            return -1

        # Create new coordinate Object
        new_coord = Coordinate(float(lat_str), float(lng_str))
        return new_coord