from socket import *

HOST = ''
PORT = 6050

ADDR = (HOST, PORT)

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect(ADDR)

i = True

while i:
	clientResponse = raw_input("Enter a city or country name: ")
	clientSocket.send(clientResponse)
	print"(waiting server...)"

	#max data that can be received, 1024bytes
	reply = clientSocket.recv(1024)
	if reply:
		print "Server:", repr(reply)
	else:
		print "Connection has been lost :("
		clientSocket.close()
		i = False

clientSocket.close()