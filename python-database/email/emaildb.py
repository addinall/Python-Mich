# vim: set expandtab tabstop=4 shiftwidth=4 autoindent:
#
# File:   emaildb.py
# Mark Addinall - November 2015
# Michigan University Computer Science - Python
#
# Synopsis: 	Process a file to extract unique organisations
#		        from the From:  lines.
#		        Store in a database.
#
#


import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')                                     # kill the last run

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')                   # and re-create it

fname = raw_input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'mbox.txt'                          # lazy typists!
fh = open(fname)                                                    # error traps missing
for line in fh:
    if not line.startswith('From: ') : continue                     # only process From lines
    pieces = line.split('@')                                        # split the org from the user
    org = pieces[1].strip()
    print org                                                       # just for me

    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, )) # see if we can fetch it
    row = cur.fetchone()                                            # ie. have we seen it before
    if row is None:                                                 # Nope
                                                                    # insert it into database
        cur.execute('''INSERT INTO Counts (org, count)             
                VALUES ( ?, 1 )''', ( org, ) )
    else : 
        cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?', 
            (org, ))                                                # yes, increment counter
    conn.commit()                                                   # write transactions


# this is just to test the result against the expected exam result

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
print "--------------------------------"
print "TOP TEN
print "--------------------------------"


for row in cur.execute(sqlstr) :
    print str(row[0]), row[1]

cur.close()

