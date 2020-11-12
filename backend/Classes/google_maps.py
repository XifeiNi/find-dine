from .api import API
from .place import Place
from .coordinate import Coordinate
import requests
import re
class Google_Maps(API):

    def get_distance(self, origin, dest, mode):
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
        # Try to Parse String, otherwise return Error
        try:
            dis_str = json_response['rows'][0]['elements'][0]['distance']['text']
            print(dis_str)

            # Get kms
            m = re.search(r'(\d*)\.(\d*) km', dis_str)
            if(m != None):
                # distance = 1.609344*int((m.group(1)))
                string_distance = m.group(1)+"."+ m.group(2)
                # distance = float((m.group(1)))
                # print(float(m.group(2)))
                distance = float(string_distance)


        except:
            return -1

        return distance

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