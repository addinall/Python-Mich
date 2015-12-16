# little HTML scraper
# Mark Addinall December 2015
# Uni of Michigen - Advanced Python
# Using data from the web
#
# fun little project to 
#   - enter the name of a start URL
#   - collect all the links
#   - find the nth link embedded in the URL
#   - follow that link
#   - iterate N times
#   - report the last link
#
# This forms the basis of a web crawler in PYTHON


import urllib
from BeautifulSoup import *

url 	= raw_input('Enter URL - ')
start 	= int(raw_input('Start Index - '))
loop 	= int(raw_input('Loop times - '))

def fetch(url):
	''' 	fetch a URL
		read the HTML
		parse it for href tags
		return a list of found tags '''

	print 'Retrieving: ' + url 
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	tags = soup.findAll('a', href=True)
	return tags 

gtags = fetch(url)

for i in range(loop):
	gtags = fetch(gtags[start - 1]['href'])

# ----------------   EOF -------------------
