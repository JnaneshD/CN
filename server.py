# import socket programming library 
import socket 
import mysql.connector
from mysql.connector import Error

# import thread module 
from _thread import *
import threading 
msg=''
print_lock = threading.Lock() 
def registration(c,connection):
	if connection.is_connected():
		#c.send("\nPress 1 to register and 2 to login\n".encode("utf-8"))
		data=c.recv(1024)
		if(str(data.decode())=='1'):
			#c.send("You will register wait".encode("utf-8"))
			c.send("\nEnter name\n".encode("utf-8"))
			name=str(c.recv(1024).decode())
			c.send("\nEnter Phone number\n".encode("utf-8"))
			phone=str(c.recv(1024).decode())
			c.send("\nEnter Password".encode("utf-8"))
			password=str(c.recv(1024).decode())
			insert_query="""INSERT INTO User_info (Name,Phone_Number,Password) VALUES(%s,%s,%s)"""
			cursor=connection.cursor()
			args=(name,phone,password)
			cursor.execute(insert_query,args)
			c.send("\nYour Registered Succesfully\n".encode("utf-8"))
			connection.commit()
		else:
			print("2 received")
			pass
# thread fuction 
def threaded(c): 
	try:
		connection = mysql.connector.connect(host='localhost',database='sample',user='root',password='')
		if connection.is_connected():
			db_Info = connection.get_server_info()
			print("Connected to MySQL Server version ", db_Info)
			msg="You connected to database "
			registration(c,connection)
			while True: 

			# data received from client 
				data = c.recv(1024)
				print("user name received") 
				if not data: 
					print('Bye') 
					print_lock.release() 
					break
		
				user=str(data.decode())
				mySql_Create_Table_Query = "SELECT password From User_info Where Name=\""+user+"\""
				data = c.recv(1024)
				print("password received")
				if not data: 
					print('Bye') 
					print_lock.release() 
					break
				cursor = connection.cursor()
				result = cursor.execute(mySql_Create_Table_Query)
				myresult=cursor.fetchall()
				for x in myresult:
					crtpsd=str(x[0])
					print(x)
				if(crtpsd==str(data.decode())):
					#c.send("\nYour password is crt".encode('utf-8'))
					
					m=''
					movie_query="SELECT Movie_Name FROM Movie"
					cursor1 = connection.cursor()
					mres=cursor1.execute(movie_query)
					fct=cursor1.fetchall()
					for i in fct:
						#print(i)
						m+=str(i[0])+'\n'
					c.send(("\nTotal Movies running \n"+m).encode("utf-8"))
					movie_name=str(c.recv(1024).decode())
					c.send("\nHow many Seats?\n".encode("utf-8"))
					seats=str(c.recv(1024).decode())

					c.send("\nEnter show number like 1 2 3 4\n".encode("utf-8"))
					show=str(c.recv(1024).decode())
					Booking_query="""INSERT INTO Booking (User_id,Movie_Name,Show_Number,Number_of_seats) VALUES(%s,%s,%s,%s)"""
					args=(user,movie_name,show,seats)
					cursor=connection.cursor()
					result=cursor.execute(Booking_query,args)
					connection.commit()
					c.send("\n Booking Succesful\n".encode("utf-8"))
				#c.send(msg.encode('utf-8'))
				else:
					c.send("\nPassword is incorrect".encode('utf-8'))
				

			# connection closed 
			c.close() 

	except Error as e:
		print("Error while connecting to MySQL", e)
	finally:
		pass
	msg="Your booking is approved"
	

def Main(): 
	
	host = "" 

	# reverse a port on your computer 
	# in our case it is 12345 but it 
	# can be anything 
	port = 12340
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	s.bind((host, port)) 
	print("socket binded to port", port) 

	# put the socket into listening mode 
	s.listen(5) 
	print("socket is listening") 

	# a forever loop until client wants to exit 
	while True: 

		# establish connection with client 
		c, addr = s.accept() 

		# lock acquired by client 
		print_lock.acquire() 
		print('Connected to :', addr[0], ':', addr[1]) 

		# Start a new thread and return its identifier 
		start_new_thread(threaded, (c,)) 
	s.close() 


if __name__ == '__main__': 
	Main() 

