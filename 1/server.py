'''
ASTHA PRIYA 
CS - A
20219024
TCP Client-Server Program
'''

import socket

port = 12456

s = socket.socket()
s.bind(('192.168.10.129', port))
s.listen(5)

print("TCP Server is running...")

while True:
	c, addr = s.accept()
	msg = input("Message to client: ")
	c.send(msg.encode())
	c.close()
	break

'''
OUTPUT:
TCP Server is running...
Message to client: hi, this is astha
'''
