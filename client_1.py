import socket 
from tkinter import *  
import time
host = '127.0.0.1'
port = 12344
x=1
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

x=0
reg=Tk()
reg.title('Registration')
reg.geometry('650x350')
rlabel1=Label(reg,text="Enter your name :",font=("calibri",14))
rlabel2=Label(reg,text="Enter password :",font=("calibri",14))
rlabel3=Label(reg,text="Enter you Phone no :",font=("calibri",14))
rlabel4=Label(reg,text="*All fields are neccesary *",font=("calibri",14))
rlabel5=Label(reg,text=" ",font=("calibri",14))
rentry1=Text(reg,width=20,height=2,font=("calibri",12))
rentry2=Text(reg,width=20,height=2,font=("calibri",12))
rentry3=Text(reg,width=20,height=2,font=("calibri",12))
rlabel1.grid(column=0,row=0)
rlabel2.grid(column=0,row=1)
rlabel3.grid(column=0,row=2)
rentry1.grid(column=1,row=0)
rentry2.grid(column=1,row=1)
rentry3.grid(column=1,row=2)
rlabel5.grid(column=1,row=4)
rlabel4.grid(column=1,row=5)
o=dict()
def regsr():
	s.send("1".encode())
	time.sleep(1)
	nam=rentry1.get("1.0","end-1c")
	pas=rentry2.get("1.0","end-1c")
	ph=rentry3.get("1.0","end-1c")
	s.send(nam.encode())
	time.sleep(1)
	s.send(pas.encode())
	time.sleep(1)
	s.send(ph.encode())
	reg.destroy()
def log():
	s.send("2".encode())
	reg.destroy()
bt=Button(reg,text="Submit",command=regsr,font=("calibri",13))
btlg=Button(reg,text="Login?",command=log,font=("calibri",13))
btlg.grid(column=1,row=3)
bt.grid(column=0,row=3)
reg.mainloop()
window=Tk()
window.title("Movie Booking System")
window.geometry('380x300')
lbel=Label(window,text="User Name :",font=("calibri",15))
lbel.grid(column=1,row=1)
lbel_1=Label(window,text="Password :",font=("calibri",15))
lbel_1.grid(column=1,row=2)
lbel_2=Label(window,text="",font=("calibri",13))
one_e=Entry(window,width=13,font=("calibri",13))
lbel_2.grid(column=1,row=3)
one_e.grid(column=2,row=1)
two_e=Entry(window,width=13,font=("calibri",13))
two_e.grid(column=2,row=2)
def sec():
	mov=one_e.get()
	seats=int(two_e.get())
	if mov in o.keys():
		available=o[mov]
		if((available-seats)>0):
			s.send(one_e.get().encode())
			time.sleep(1)
			s.send(two_e.get().encode())
			data=s.recv(1024)
			lbel.configure(text=str(data.decode()),font=("calibri",13))
			lbel_1.grid_remove()
			one_e.grid_remove()
			two_e.grid_remove()
			Butn.grid_remove()
		else:
			one_e.delete(0,END)
			two_e.delete(0,END)
			lbel_2.grid(column=1,row=6)
			lbel_2.configure(text="**Please enter from available seats**")
	else:
		one_e.delete(0,END)
		two_e.delete(0,END)
		lbel_2.grid(column=1,row=6)
		lbel_2.configure(text="**Please enter from available movies**")
	
def submt():
	window.geometry('480x470')
	user=str(one_e.get())
	pasd=str(two_e.get())
	s.send(user.encode("utf-8"))
	time.sleep(1)
	s.send(pasd.encode("utf-8"))
	data=s.recv(1024)		
	if(str(data.decode("utf-8"))=="1"):
		time.sleep(1)
		data=s.recv(1024)
		lbel.configure(text=str(data.decode("utf-8")))
		mov=str(data.decode("utf-8")).strip()
		gg=mov.split(".")
		hh=[]
		for i in range(1,4):
			hh.append(gg[i])
		for i in hh:
			k=i.split(":")
			k1=int(k[1])
			o[k[0]]=k1
		print(o)
		one_e.delete(0,END)
		two_e.delete(0,END)
		one_e.grid(column=1,row=2)
		two_e.grid(column=1,row=3)
		lbel_1.configure(text="\nEnter movie name \n \n\nEnter seats")
		Butn.configure(command=sec)
	else:
		one_e.delete(0,END)
		two_e.delete(0,END)
		lbel.configure(text="Wrong Password\n User name")
	#time.sleep(2)
	#window.destroy()
Butn=Button(window,text="SUBMIT",command=submt,font=("calibri",14))
Butn.grid(column=1,row=5)
window.mainloop()
s.close() 

