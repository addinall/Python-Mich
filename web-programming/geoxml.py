# vim: set expandtab tabstop=4 shiftwidth=4 autoindent smartindent:
#
# File:   geoxml.py
# Mark Addinall - November 2015
# Michigan University Computer Science - Python
#
# Synopsis:
# This code accesses a RESTful web service
# mainly a GOOGLE location finder, but this
# time we want to consume the data using
# the XML data protocol
#

import urllib
import xml.etree.ElementTree as ET

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
    print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    print 'Retrieved',len(data),'characters'
    print data
    tree = ET.fromstring(data)


    results = tree.findall('result')
    lat = results[0].find('geometry').find('location').find('lat').text
    lng = results[0].find('geometry').find('location').find('lng').text
    location = results[0].find('formatted_address').text

    print 'lat',lat,'lng',lng
    print location
