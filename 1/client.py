'''
ASTHA PRIYA 
CS - A
20219024
TCP Client-Server Program
CLIENT
'''

import socket

s = socket.socket()
port = 12456
s.connect(('192.168.10.129',port))
print(f"Recieved From SERVER: {s.recv(1024).decode()}")
s.close()

'''
OUTPUT:
Recieved From SERVER: hi, this is astha
'''
