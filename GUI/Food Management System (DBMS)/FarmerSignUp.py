from tkinter import *
import pymysql.cursors
import random
import Login as L
import PostLogin as P
import Update as U

root = Tk()
root.geometry('500x750')
root.title("Registration form for FARMER")

#GENERATING RANDOM UNID
def create_unid():
	return(random.randint(1001, 1999))

#VARIABLE INITIALIZATIONS
unid= create_unid()
name= StringVar()
mobile= StringVar()
crop_name= StringVar()
soil_type= StringVar() 
weight_per_yeild= IntVar()
cost_per_quintal= IntVar()
aadhar= StringVar()
city= StringVar()
nstate= StringVar()
pincode= IntVar()
password= StringVar()
c=StringVar()

def Back():
    PSU.destroy()
    root.deiconify()

#DATABASE CONNECTIVITY
def database_conn():

	conn= pymysql.connect(host='localhost',user='root',password='WeRock',db='foodchainmanagement',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
	
	print ("Connected successfully!")

	if(conn):

		unid=int(create_unid())
		name=str(entry_1.get())
		mobile=str(entry_2.get())
		crop_name=str(entry_3.get())
		soil_type=str(entry_4.get()) 
		weight_per_yeild=int(entry_5.get())
		cost_per_quintal=int(entry_6.get())
		aadhar=str(entry_7.get())
		city=str(entry_8.get())
		state=str(c.get())
		pincode=int(entry_10.get())
		password=str(entry_11.get())
		print(unid,name,mobile,crop_name,soil_type,weight_per_yeild,cost_per_quintal,aadhar,city,nstate,pincode,password)
		
		try:
			with conn.cursor() as cursor:
				insert1 = "INSERT INTO Farmer (Unid,Name,Mobile,Crop_name,Soil_type,Weight_per_yeild,Cost_per_quintal,Aadhar,City,State,Pincode,Password) VALUES(%d,'%s','%s','%s','%s',%d,%d,'%s','%s','%s',%d,'%s')" % (unid,name,mobile,crop_name,soil_type,weight_per_yeild,cost_per_quintal,aadhar,city,state,pincode,password)
				cursor.execute(insert1)
				conn.commit()
				print("Values Inserted Successfully!")

		finally:
			conn.close()

	else:
		print("Connection Unsuccesfull.")

	global PSU
	PSU = Toplevel()
	PSU.title("Successfully logged in!")
	width = 400
	height = 200
	screen_width = root.winfo_screenwidth()
	screen_height = root.winfo_screenheight()
	x = (screen_width/2) - (width/2)
	y = (screen_height/2) - (height/2)
	root.resizable(0, 0)
	PSU.geometry("%dx%d+%d+%d" % (width, height, x, y))

	lbl_home = Label(PSU, text="Welcome! %s" % str(unid), font=('times new roman', 20)).pack()

	btn_1= Button(PSU, text='Update', width=20, command=U.UpdateValues).place(x=100,y=100)

	btn_cont = Button(PSU, text='View All Data', width=20, command=P.FarmerView).place(x=20, y= 150)
	btn_back = Button(PSU, text='Logout', width=20, command=Back).place(x=200, y=150)

def quit_func():
	root.withdraw()
	import HomePage

 
#GUI CODE
label_0 = Label(root, text="FARMER's form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="Full Name",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root,textvar=name)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Mobile no.",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(root,textvar=mobile)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Crop Name",width=20,font=("bold", 10))
label_3.place(x=70,y=230)

entry_3 = Entry(root,textvar=crop_name)
entry_3.place(x=240,y=230)

label_4 = Label(root, text="Soil type",width=20,font=("bold", 10))
label_4.place(x=68,y=280)

entry_4 = Entry(root,textvar=soil_type)
entry_4.place(x=240,y=280)

label_5 = Label(root, text="Weight per yeild",width=20,font=("bold", 10))
label_5.place(x=68,y=330)

entry_5 = Entry(root,textvar=weight_per_yeild)
entry_5.place(x=240,y=330)

label_6 = Label(root, text="Cost per quintal",width=20,font=("bold", 10))
label_6.place(x=68,y=380)

entry_6 = Entry(root,textvar=cost_per_quintal)
entry_6.place(x=240,y=380)

label_7 = Label(root, text="Aadhar no.",width=20,font=("bold", 10))
label_7.place(x=68,y=430)

entry_7 = Entry(root,textvar=aadhar)
entry_7.place(x=240,y=430)

label_8 = Label(root, text="City",width=20,font=("bold", 10))
label_8.place(x=68,y=480)

entry_8 = Entry(root,textvar=city)
entry_8.place(x=240,y=480)

label_9 = Label(root, text="State",width=20,font=("bold", 10))
label_9.place(x=70,y=530)

list1 = ['Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chhattisgarh','Goa', 'Gujrat', 'Haryana', 'Himachal Pradesh', 'Jammu & Kashmir', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Tamil Nadu', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal' ];

droplist=OptionMenu(root,c, *list1)
droplist.config(width=15)
c.set('Select your State') 
droplist.place(x=240,y=530)

label_10 = Label(root, text="Pincode",width=20,font=("bold", 10))
label_10.place(x=68,y=580)

entry_10 = Entry(root,textvar=pincode)
entry_10.place(x=240,y=580)

label_11 = Label(root, text="Password",width=20,font=("bold", 10))
label_11.place(x=68,y=630)

entry_11 = Entry(root,show="*",textvar=password)
entry_11.place(x=240,y=630)

Button(root, text='Submit',width=20,bg='green',fg='white', command=database_conn).place(x=120,y=680)
Button(root, text='Cancel',width=20,bg='red',fg='white', command=quit_func).place(x=280,y=680)

root.mainloop()