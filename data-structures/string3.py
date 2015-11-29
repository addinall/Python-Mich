# vim: set expandtab tabstop=4 shiftwidth=4 autoindent smartindent:
#
# File:   string3.py
# Mark Addinall - November 2015
# Michigan University Computer Science - Python
#
# Synopsis: 
# Open the file mbox-short.txt and read it line by line. 
# When you find a line that starts with 'From ' like the following line:
#    From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#    You will parse the From line using split() and print out the 
# second word in the line (i.e. the entire address of the person who 
# sent the message). Then print out a count at the end.

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
words = list()

for line in fh:
    if line.startswith("From "):
        count += 1
        words =line.split()
        print words[1]

print "There were", count, "lines in the file with From as the first word"

