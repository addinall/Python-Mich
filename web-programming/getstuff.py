# vim: set expandtab tabstop=4 shiftwidth=4 autoindent smartindent:
#
# File:   getstuff.py
# Mark Addinall - November 2015
# Michigan University Computer Science - Python
#
# Synopsis:
# This program makes an old fashoined BSD SOCKET
# connection.  Most of the students have never seen a socket before
# so it is pretty exiting for them!!!
#

import socket

mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('www.pythonlearn.com',80))
mysock.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')

while True:
	data=mysock.recv(512)
	if(len(data)<1):
		break
	print data;

mysock.close()
