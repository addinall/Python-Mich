# vim: set expandtab tabstop=4 shiftwidth=4 autoindent smartindent:
#
# File:   list1.py
# Mark Addinall - November 2015
# Michigan University Computer Science - Python
#
# Synopsis:
# Open the file romeo.txt and read it line by line. For each line, 
# split the line into a list of words using the split() function. 
# The program should build a list of words. For each word on each 
# line check to see if the word is already in the list and if 
# not append it to the list. When the program completes, 
# sort and print the resulting words in alphabetical order.


fname = raw_input("Enter file name: ")
fh = open(fname)

lst = list()                    # out final collection
words = list()                  # words per line

for line in fh:                 # read file by line
    words = line.split()        # split on any white
    for word in words:          # examine each word
        if not word in lst:     # if it isn't in our collection
            lst.append(word)    # pop it in
lst.sort()                      # sort alphabeticall A-Z
print lst                       # and show the world


