from tkinter import *
import Login as L

def NewWindow():
	if variable.get()=='Farmer':
		if(int(var.get())==1):
			quit_f()
			import FarmerSignUp
		elif(int(var.get())==2):
			quit_f()
			L.LoginForm()

	elif variable.get()=='Distributor':
		master.destroy()
		root2=Tk()
		root2.mainloop()

	elif variable.get()=='Retailer':
		master.quit()
		root3=Tk()
		root3.mainloop()	

def	quit_f():
	master.destroy()

master=Tk()
master.geometry('375x250')
master.title("WELCOME")

Label(master, text="Food Chain Management",width=20,font=("bold",20)).place(x=20,y=20)

variable=StringVar(master)
variable.set("Select Role")
option=OptionMenu(master, variable, "Farmer", "Distributor", "Retailer")
option.place(x=130,y=70)

var=IntVar()
Radiobutton(master, text="New User",padx = 5, variable=var, value=1).place(x=80,y=120)
Radiobutton(master, text="Registered",padx = 20, variable=var, value=2).place(x=175,y=120)

Button(master,text='Proceed',width=10,command=NewWindow).place(x=90,y=170)
Button(master,text='Quit',width=10,command=quit_f).place(x=190,y=170)

master.mainloop()
