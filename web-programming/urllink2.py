# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *

url =  'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_200690.html'
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)
total = 0
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
   # Look at the parts of a tag
   total += int(tag.contents[0])
print total

