'''
ASTHA PRIYA 
CS - A
20219024
SUBSTITUTION CIPHER DECRYPTION
'''

import socket

def decode(cipher,key):
	lkey = len(key)
	ltext = len(cipher)
	plain = ''
	alphabets = 'abcdefghijklmnopqrstuvwxyz'
	c=0
	while(c<ltext):
		ch = cipher[c]
		d = 0
		while(d<len(alphabets)):
			if alphabets[d] == ch:
				break
			d+=1
		if(d>lkey-1):
			d-=lkey
		else:
			d+=(len(alphabets)-lkey)

		plain+=alphabets[d]
		c+=1
	return plain

port = 12345
localip = '127.0.0.1'
s = socket.socket()

s.connect((localip,port))
dat = s.recv(1024).decode()
d = dat.split(' ')
cipher = d[0]
key = d[1]

print("Ciphertext: ", cipher)
plain = decode(cipher,key)
print("PlainText: ", plain)

'''
$ python3 sub_de.py
Ciphertext:  cuvjc
PlainText:  astha
'''
