# geotests.py
# Mark Addinall Novemeber 2015
# Advanced Python - Using Web Data
# Michigan University
#
# Little program that uses GOOGLE geo-location data
# Acessing a RESTful service that returns JSON data

import urllib
import json 

serviceurl = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/geojson?'

while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break
    						# first encode the REST
						# request as per the GOOGLE API

    url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})

    print 'Retrieving', url
    uh = urllib.urlopen(url)			# get a file handle
    data = uh.read()				# fetch the data as a string
    print 'Retrieved',len(data),'characters'

    try:					# we could get a partial return
	    js = json.loads(str(data))		# unde heavy load so throw
    except:					# an exception and
	    js = None				# NULLify out Python dictionary

    if 'status' not in js or js['status'] != 'OK':
            print '==== Failure To Retrieve ===='
            print data
            continue				# and have another go at it

    print js['results'][0]['place_id']		# this is what the exam requires 

# ----------------------- EOF ------------------

