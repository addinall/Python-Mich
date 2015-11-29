# jsontest.py
# Mark Addinall Novemeber 2015
# Advanced Python - Using Web Data
# Michigan University
#
# Little program that uses json lib to build and access a JSON dataset


import urllib
import json 


serviceurl = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/'


while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + address			# just sick of typing long names
    print 'Retrieving', url
    uh = urllib.urlopen(url)			# get a file handle
    data = uh.read()				# fetch the data as a string
    print 'Retrieved',len(data),'characters'

    jstuff = json.loads(data)			# deserialize into Python
    en = 0					# number of occurences
    sum = 0					# total number of counts

    for item in jstuff['comments']:
	    sum += item['count']		# sum fictional number of comments
	    en += 1				# increment N counter

    print 'Count: ' + str(en)			# and tell people
    print sum 
# ----------------------- EOF ------------------

