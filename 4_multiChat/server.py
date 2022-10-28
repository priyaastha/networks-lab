'''
ASTHA PRIYA 
CS - A
20219024
TCP Client-Server Program
'''

from _thread import *
import socket, sys


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

IP = "192.168.10.129"
PORT = 5050

server.bind((IP, PORT))

name_map = {}


server.listen(100)

list_of_clients = []
 
def clientthread(conn, addr):
    conn.send("Welcome to this chatroom!".encode())
    while True:
       	try:
            message = conn.recv(2048)
            if message:
                print ("<" + name_map[addr[0]] + "> " + str(message.decode()))
                message_to_send = "<" + name_map[addr[0]] + "> " + str(message.decode())
                broadcast(message_to_send, conn)
            else:
                remove(conn)
        except Exception as e:
            print(e)
            continue

def broadcast(message, connection):
    for clients in list_of_clients:
        if clients!=connection:
            try:
                clients.send(message.encode())
            except:
                clients.close()
                remove(clients)
 
def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)
 
while True:
    conn, addr = server.accept()
    name = conn.recv(2048).decode()
    name_map[addr[0]] = name
    list_of_clients.append(conn)
    print (name_map[addr[0]] + " connected")
    start_new_thread(clientthread,(conn,addr))    
 
conn.close()
server.close()

'''
OUTPUT:

astha connected
shru connected
riya connected
<riya> hi

<astha> hello

<shru> hey
'''

