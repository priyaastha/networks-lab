'''
ASTHA PRIYA 
CS - A
20219024
HAMMMING CODE SERVER
'''

# First of all import the socket library
import socket

def detectError(arr, nr):
	n = len(arr)
	res = 0

	 
	for i in range(nr):
		val = 0
		for j in range(1, n + 1):
			if(j & (2**i) == (2**i)):
				val = val ^ int(arr[-1 * j])

	 

		res = res + val*(10**i)

	 
	return int(str(res), 2)
def calcRedundantBits(m):

	 
	for i in range(m):
		if(2**i >= m + i + 1):
			return i
s = socket.socket()
print("Socket successfully created")

# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 12345

s.bind(('', port))
print("socket binded to %s" % (port))
# put the socket into listening mode
s.listen(5)
print("socket is listening")


while True:
	# Establish connection with client.
	c, addr = s.accept()
	print('Got connection from', addr)

	# Get data from client
	data = c.recv(1024)

	print("Received data :", data.decode())

	if not data:
		break

	 
 
	arr = '11101001110'
	m = len(data)
	r = calcRedundantBits(m)
	print("Error Data is " + arr)
	correction = detectError(arr, r)
	if(correction==0):
		c.sendto(("No errors found in data :)").encode(), ('127.0.0.1', 12345))
	else:
		temp=len(arr)-correction+1
		st="The position of error is "+str(temp)
		st=st+" from the left"
		c.sendto((st).encode(), ('127.0.0.1', 12345))

	 

	c.close()


'''
$ python3 server.py
Socket successfully created
socket binded to 12345
socket is listening
Got connection from ('127.0.0.1', 38474)
Received data : 010100011100
Error Data is 11101001110
'''

