'''
ASTHA PRIYA 
CS - A
20219024
TCP Client-Server Program
Client
'''

import socket

localip = "127.0.0.1"
port = 12367

c = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

msg = input("CLIENT: ")
c.sendto(str.encode(msg), (localip, port))

msgaddrpair = c.recvfrom(1024)
msg = msgaddrpair[0]
print(f"SERVER: {msg.decode()}")

'''
OUTPUT:

CLIENT: hi, this is your message
SERVER: hello, i received
'''
