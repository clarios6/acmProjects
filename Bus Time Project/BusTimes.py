#Carlos Larios-Solis
#Made using Metro's API
#Used "Moovit" app to help verify that the bus times were correct

import json     #Library is a JSON encoder and decoder
import urllib3  #HTTP client for Python
import time

#PoolManager object will handle all the Requests
http = urllib3.PoolManager()

busLineCounter = 0
busLineMax = 9

while 1:
    # url to get the json from
    url = 'http://api.metro.net/agencies/lametro/stops/708/predictions/'

    # Make a GET request to the URL you generated. The request will return a JSON file
    file = http.request('GET', url)

    # json.loads function will take our JSON file and parse it into readable strings
    parsed_json = json.loads(file.data.decode('utf-8'))

    #gets the amount of items parsed_json holds
    #print(len(parsed_json["items"]))

    for x in range(0, len(parsed_json["items"])):
        #print(x)

        # print(parsed_json)

        # Variables access specific JSON values
        bus = parsed_json["items"][x]["route_id"]
        busTimeInMin = parsed_json["items"][x]["minutes"]
        #if busTimeInMin < 60:
        print("Line " + str(bus) + " is departing in: " + str(busTimeInMin) + " minutes.")

    time.sleep(10)