'''
ASTHA PRIYA 
CS - A
20219024
TCP Client-Server Program
Server
'''

import socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
LOCALHOST = '127.0.0.1'
port = 9990

server_socket.bind((LOCALHOST,port))
server_socket.listen(5)

print("Server started...")

client_sockets,addr=server_socket.accept()
while True:
    msg_received = client_sockets.recv(1024)
    msg_received = msg_received.decode()
    print("Client:", msg_received)
    
    msg_send = input("Me:")
    client_sockets.send(msg_send.encode("ascii"))

client_sockets.close()

'''
OUTPUT:

Server started...
Client: hi
Me:hello
Client: this is a msg
Me:i received your msg
Client: waiting for answer
Me:??
'''
