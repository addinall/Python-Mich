# vim: set expandtab tabstop=4 shiftwidth=4 autoindent smartindent:
#
# File:   geojson.py
# Mark Addinall - November 2015
# Michigan University Computer Science - Python
#
# Synopsis:
# This little programm accesses a RESTful Web
# service that has the same API interface as the
# GOOGLE product.  It was duplicated to remove students from
# ACTUAL GOOGLE data when experimenting in pracs
#
# It asks the user for a location - University of Michigan
# Terminates on an empty response
# Encodes the URL requires with the GOOGLE API flags
# Read the URL data into a Python STRING
# Load the STRING into a JSON object
# Teminate if the JSON data is bad
# Grabbs retrieved data from the JSOM objects
# Prints the data o screen
# LOOP


import urllib
import json

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'

    try: js = json.loads(str(data))
    except: js = None
    if 'status' not in js or js['status'] != 'OK':
        print '==== Failure To Retrieve ===='
        print data
        continue

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print 'lat',lat,'lng',lng
    location = js['results'][0]['formatted_address']
    print location

