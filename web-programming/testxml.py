# testxml.py
# Mark Addinall Novemeber 2015
# Advanced Python - Using Web Data
# Michigan University
#
# Little program that uses lxml to build and access an XML doc ument


import urllib
import lxml.etree as ET


serviceurl = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/'


while True:
    address = raw_input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + address			# just sick of typing long names
    print 'Retrieving', url
    uh = urllib.urlopen(url)			# get a file handle
    data = uh.read()				# fetch the data as a string
    print 'Retrieved',len(data),'characters'

    root = ET.fromstring(data)			# build the tree and root node

    counts = root.findall('.//count')		# find all of the <count> child nodes
    en     = len(counts)			# how many found
    sum    = 0

    for node in counts:
	    sum += int(node.text)		# calculate sum of <count>values</count>

    print 'Count: ' + str(en)			# and tell people
    print sum 
# ----------------------- EOF ------------------

