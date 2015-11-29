# vim: set expandtab tabstop=4 shiftwidth=4 autoindent smartindent:
#
# File:   string3.py
# Mark Addinall - November 2015
# Michigan University Computer Science - Python
#
# Synopsis: 
# Write a program to read through the mbox-short.txt and figure 
# out who has the sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of 
# those lines as the person who sent the mail. The program 
# creates a Python dictionary that maps the sender's mail address 
# to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through 
# the dictionary using a maximum loop to find the most prolific committer.


fname = raw_input("Enter file name: ")  
if len(fname) < 1 : fname = "mbox-short.txt"        # everyone is tired of
                                                    # typing huge filenames
fh = open(fname)

words = list()
hist = dict()                                       # our histogram

# The histogram is going to have the structure
#     {key_the_email_address: count_times}


for line in fh:
    if line.startswith("From "):
        words =line.split()
        if words[1] in hist:
            hist[words[1]] += 1
        else:
            hist[words[1]] = 1

big = 0                                             # I KNOW a brute force loop
who = "TheShadow"                                   # isn't the trickiest way of
                                                    # doing this, we have max()
for p in hist:                                      # and lambda etc, but this
    if hist[p] > big:                               # is what was asked for in the
        big = hist[p]                               # specification up top.
        who = p                                     # classic swap() find
                                                    # the biggest in an unordered
print who + ' ' + str(big)                          # list.

