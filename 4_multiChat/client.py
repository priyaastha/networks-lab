'''
ASTHA PRIYA 
CS - A
20219024
TCP Client-Server Program
'''

import socket
import select
import sys
 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 2:
    print ("Correct usage: script, name")
    exit()
IP_address = "192.168.10.129"
Port = 5050
name = str(sys.argv[1]).encode()
server.connect((IP_address, Port))
 
server.send(name)

while True:
    sockets_list = [sys.stdin, server]
    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])
    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048)
            print (message.decode())
        else:
            message = sys.stdin.readline()
            server.send(message.encode())
            sys.stdout.write("<You>")
            sys.stdout.write(message)
            sys.stdout.flush()
server.close()

'''
OUTPUT:

Welcome to this chatroom!
<riya> hi

hello
<You>hello
'''

