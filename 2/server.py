'''
ASTHA PRIYA 
CS - A
20219024
TCP Client-Server Program
Server
'''

import socket

port = 12367
localip = "127.0.0.1"

s = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)
s.bind((localip,port))
print("UDP Server running...")


while True:
	msgaddrpair = s.recvfrom(1024)
	msgclient = msgaddrpair[0]
	address = msgaddrpair[1]

	print("CLIENT: {}".format(msgclient.decode()))

	msg = input("SERVER: ")
	s.sendto(msg.encode(),address)

'''
OUTPUT:

UDP Server running...
CLIENT: hi, this is your message
SERVER: hello, i received
'''
