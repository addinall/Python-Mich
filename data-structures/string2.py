# vim: set expandtab tabstop=4 shiftwidth=4 autoindent smartindent:
#
# File:   string2.py
# Mark Addinall - November 2015
# Michigan University Computer Science - Python
#
# Synopsis:  Dumb little prac 7.2
# Write a program that prompts for a file name, then opens that 
# file and reads through the file, looking for lines of the form:
#     X-DSPAM-Confidence:    0.8475
#     Count these lines and extract the floating point values from 
# each of the lines and compute the average of those values and 
# produce an output as shown below.
#
# Average spam confidence: 0.750718518519
fname = raw_input("Enter file name: ")
fh = open(fname)
sum = 0
N = 0
for line in fh:
        if not line.startswith("X-DSPAM-Confidence:") : continue
        N += 1
        sum += float(line[line.find(':')+1:])
print "Average spam confidence: " + str(sum/N)

