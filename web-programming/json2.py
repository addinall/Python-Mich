# vim: set expandtab tabstop=4 shiftwidth=4 autoindent smartindent:
#
# File:   json2.py
# Mark Addinall - November 2015
# Michigan University Computer Science - Python
#
# Synopsis:
# Just a test of the json library.
#

import json
input = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Chuck"
  } 
]'''

info = json.loads(input)
print 'User count:', len(info)

for item in info:
    print 'Name', item['name']
    print 'Id', item['id']
    print 'Attribute', item['x']

