# vim: set expandtab tabstop=4 shiftwidth=4 autoindent smartindent:
#
# File:   string1.py
# Mark Addinall - November 2015
# Michigan University Computer Science - Python
#
# Synopsis:  Dumb little prac 7.1
# Read a file and print it in upper case
#
fname = raw_input("Enter file name: ")
fh = open(fname)
for l in fh:
	    print l.strip().upper()
	        
