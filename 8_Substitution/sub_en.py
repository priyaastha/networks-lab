'''
ASTHA PRIYA 
CS - A
20219024
SUBSTITUTION CIPHER ENCRYPTION
'''

import socket

def encode(plain,key):
	lkey = len(key)
	ltext = len(plain)
	cipher = ''
	alphabets = 'abcdefghijklmnopqrstuvwxyz'
	c=0
	while(c<ltext):
		ch = plain[c]
		d = 0
		while(d<len(alphabets)):
			if alphabets[d] == ch:
				break
			d+=1
		if(d<len(alphabets)-lkey):
			d+=lkey
		else:
			d-=(len(alphabets)-lkey)

		cipher+=alphabets[d]
		c+=1
	return cipher
s = socket.socket()
print ("Socket Successfully connected")

port = 12345
localip = '127.0.0.1'
s.bind(('',port))
print("socket binded to port ",port)

s.listen(5)
print("Socket is listeing")

c,addr = s.accept()
print("Connection from ", addr)

plain = input("Enter the message: ")
key = input("Enter the key: ")

cipher = encode(plain,key)
print("CipherText: ", cipher)
finaldat = cipher + ' ' + key
c.sendto((finaldat).encode(),(localip,port))

c.close()

'''
$ python3 sub_en.py
Socket Successfully connected
socket binded to port  12345
Socket is listeing
Connection from  ('127.0.0.1', 60884)
Enter the message: astha
Enter the key: qw
CipherText:  cuvjc
'''

