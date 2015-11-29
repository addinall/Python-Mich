# vim: set expandtab tabstop=4 shiftwidth=4 autoindent smartindent:
#
# File:   freq`.py
# Mark Addinall - November 2015
# Michigan University Computer Science - Python
#
# Synopsis: 
# Open the file mbox-short.txt and read it line by line. 
# When you find a line that starts with 'From ' like the following line:
#    From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# figure out the distribution by hour of the day for each of the messages.

fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)

words = list()                          # same old list of words per line
times = list()                          # new list of HH MM SS time of posting
freq = dict()                           # time: frequent

for line in fh:
    if line.startswith("From "):        # standard stuff we have been doing all
        words =line.split()             # dat.  This all looks rather upgly.
        times = words[5].split(':')     # [5] is a date string NN:NN:NN
        if times[0] in freq:            # build the KEYS on the hour value
            freq[times[0]] += 1         # and keep track of the frequency
        else:
            freq[times[0]] = 1          # create in not there

for k, v in sorted(freq.items()):       # sort the dict on the key
    print k, v                          # for an ordered output.



