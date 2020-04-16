# import socket programming library 
import socket 
from _thread import *
import threading 
import time
print_lock = threading.Lock() 

# thread fuction 
def threaded(c):
	data=c.recv(1024)
	if(str(data.decode())=="1"):
		data=c.recv(1024)
		name=str(data.decode())
		data=c.recv(1024)
		pasd=str(data.decode())
		data=c.recv(1024)
		ph=str(data.decode())
		file = open(name+".txt", "w")
		file.write(name+":"+pasd)
		file.close()
	else:
		pass
	x=1
	while x>0:
		data = c.recv(1024)
		password = c.recv(1024)
		print("both recieved")
		login1=str(data.decode())
		login2=str(password.decode())
		print(str(data.decode()))
		print(str(password.decode()))
		file = open(login1+".txt", "r")
		data = file.readline()
		file.close()
		if data == login1+":"+login2:
			print("Oho its working")
			c.send("1".encode("utf-8"))
			time.sleep(1)
			file = open("Venom.txt","r")
			Venom=file.readline()
			file.close()
			file = open("Joker.txt","r")
			Joker=file.readline()
			file.close()
			file = open("Villain.txt","r")
			Villain=file.readline()
			file.close()
			c.send(("Total Movies Running are \n(format)Movie:Seats Left\n.Venom:"+Venom+"\n.Joker:"+Joker+".Villain:"+Villain).encode("utf-8"))
			data=c.recv(1024)
			movie=str(data.decode())
			data=c.recv(1024)
			seats=str(data.decode())
			seat=int(data)
			print("Seats entered"+seats)
			file=open(movie+".txt","r")
			seatdata=file.readline()
			seats_rem=int(seatdata)
			file.close()
			seats_written=seats_rem-seat
			print(str(seats_written))
			file=open(movie+".txt","w")
			file.write(str(seats_written))
			file.close()
			file=open(login1+"_ticket.txt","w")
			file.write("Movie Name: "+movie+"\n Number of Tickets :"+seats)
			file.close()
			c.send(("Your booking is confirmed :\n Movie :"+movie+"\n seats: "+seats).encode())
			x=0
		
		else:
			pass
			c.send("2".encode("utf-8"))
	c.close() 
def Main(): 
	host = "" 
	port = 12344
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	s.bind((host, port)) 
	print("socket binded to port", port) 
	s.listen(5) 
	print("socket is listening") 
	while True: 
		c, addr = s.accept() 

		# lock acquired by client 
		#print_lock.acquire() 
		print('Connected to :', addr[0], ':', addr[1]) 

		# Start a new thread and return its identifier 
		start_new_thread(threaded, (c,)) 
	s.close() 
if __name__ == '__main__': 
	Main() 

