# Import socket module 
import socket 


def Main(): 
	# local host IP '127.0.0.1' 
	host = '127.0.0.1'

	# Define the port on which you want to connect 
	port = 12340

	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

	# connect to server on local computer 
	s.connect((host,port)) 

	# message you send to server 
	data=s.recv(1024)
	inp=str(input(str(data.decode('utf-8'))))
	s.send(inp.encode("utf-8"))
	if(inp=="1"):

		data=s.recv(1024)
		inp=str(input(str(data.decode('utf-8'))))
		s.send(inp.encode("utf-8"))
		data=s.recv(1024)
		inp=str(input(str(data.decode('utf-8'))))
		s.send(inp.encode("utf-8"))
		data=s.recv(1024)
		inp=str(input(str(data.decode('utf-8'))))
		s.send(inp.encode("utf-8"))
		data=s.recv(1024)
		print(str(data.decode("utf-8")))
	while True: 
		message = str(input("\nTell me who you are (1 to quit)\n\n"))
		# message sent to server 
		if(message=='1'):
			break
		s.send(message.encode('ascii')) 

		# messaga received from server 
		#data = s.recv(1024) 
		#print('\nReceived from the server : ',str(data.decode('utf-8'))) 
		message = str(input("\nTell password \n"))
		s.send(message.encode('utf-8'))
		data = s.recv(1024)
		# print the received message 
		# here it would be a reverse of sent message 
		inp=str(input('\nReceived from the server :'+str(data.decode('utf-8'))))
		s.send(inp.encode("utf-8"))
		data=s.recv(1024)#moviename
		inp=str(input(str(data.decode('utf-8'))))
		s.send(inp.encode("utf-8"))#seats
		data=s.recv(1024)
		inp=str(input(str(data.decode('utf-8'))))
		s.send(inp.encode("utf-8"))
		data=s.recv(1024)#show
		print(data.decode())
		# ask the client whether he wants to continue 
		#ans = input('\nDo you want to continue(y/n) :') 
		#if ans == 'y': 
		#	continue
		#else: 
		#break
	# close the connection 
	s.close() 

if __name__ == '__main__': 
	Main() 

