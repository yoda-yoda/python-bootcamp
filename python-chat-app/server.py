from socket import *

HOST = gethostbyname(gethostname())
print "server is now running...:",HOST
PORT = 6050

ADDR = (HOST, PORT)

dictionary = dict(
	nairobi = 'kenya',
 	cairo = 'egypt',
 	mogadishu = 'somalia',
 	kigali = 'rwanda',
 	capeTown = 'south africa',
 	paris = 'france',
 	rome = 'italy',
 	london = 'britain',
 	kampala = 'uganda',
 	lagos = 'nigeria',
 	daaresalaam = 'tanzania',
 	brasil = 'brazil',
 	dakar = 'senegal' 
  )

cityDictionary = dict(
	kenya = 'nairobi',
	egypt = 'cairo',
	somalia = 'mogadishu',
	nigeria= 'lagos',
	france = 'paris',
	brazil = 'brasil',
	britain = 'london',
	uganda = 'kampala',
	senegal = 'dakar',
	italy = 'rome',
	ghana = 'accra',
	algeria = 'algia',
	sudan = 'khartoum',
	rwanda = 'kigali'
  )

#socket setUp -- instantiate the socket class
newSocket = socket(AF_INET, SOCK_STREAM)

#bind() takes in connectionns
newSocket.bind(ADDR)

#receive only one connection
newSocket.listen(1)

#accept the connection
connection, address = newSocket.accept()
print "New client connected:", address

	#receice data(user message) 1024 bytes using the connection
while True:
	print "waiting for message..."
	data = connection.recv(1024)
	print address,"requests: " , repr(data)


	if dictionary.__contains__(data.lower()):
		reply = "%s is the capital city of %s" % (data.capitalize(), dictionary.get(data.lower()).capitalize())

	elif cityDictionary.__contains__(data.lower()):
		reply = "%s's capital city is %s" % (data.capitalize(), cityDictionary.get(data.lower()).capitalize())

	else:
		reply = "No results found."

	#reply = "Reply: did you just say "+data.upper()
	connection.sendall(reply)


newSocket.close()







