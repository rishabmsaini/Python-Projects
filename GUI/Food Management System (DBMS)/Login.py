from tkinter import *
import pymysql.cursors
import PostLogin
import Update as U

def LoginForm():
	def Database():
	    conn= pymysql.connect(host='localhost',user='root',password='WeRock',db='foodchainmanagement',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
	    cursor = conn.cursor()
	    return conn,cursor 

	def Login(event=None):

		conn,cursor=Database()
		"""
		if USERNAME.get() == "" or PASSWORD.get() == "":
			lbl_text.config(text="Please complete the required field!", fg="red")
		else:
		"""
		un=int(username.get())
		passwrd=str(password.get())
		sql = "SELECT Name FROM FARMER WHERE Unid= %d AND Password= '%s'" % (un,passwrd)
		print("\n\n",un,"\n",passwrd,"\n",sql,"\n\n")
		cursor.execute(sql)
		if cursor.fetchone() is not None:
			HomeWindow()
			USERNAME.set("")
			PASSWORD.set("")
			lbl_text.config(text="")
		else:
			lbl_text.config(text="Invalid unique ID or password", fg="red")
			USERNAME.set("")
			PASSWORD.set("")   

		cursor.close()
		conn.close()

	def Continue():
		Home.withdraw()
		PostLogin.FarmerView()
	 
	def HomeWindow():
		global Home
		root.withdraw()
		Home = Toplevel()
		Home.title("Successfully logged in!")
		width = 400
		height = 200
		screen_width = root.winfo_screenwidth()
		screen_height = root.winfo_screenheight()
		x = (screen_width/2) - (width/2)
		y = (screen_height/2) - (height/2)
		root.resizable(0, 0)
		Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
		lbl_home = Label(Home, text="Welcome! %s" % str(username.get()), font=('times new roman', 20)).pack()

		btn_1= Button(Home, text='Update', width=20, command=U.UpdateValues).place(x=100,y=100)

		btn_cont = Button(Home, text='View All Data', width=20, command=PostLogin.FarmerView).place(x=20, y= 150)
		btn_back = Button(Home, text='Logout', width=20, command=Back).place(x=200, y=150)
	 
	def Back():
	    Home.destroy()
	    root.deiconify()


	root = Tk()
	root.title("Please Login")
	width = 400
	height = 280
	screen_width = root.winfo_screenwidth()
	screen_height = root.winfo_screenheight()
	x = (screen_width/2) - (width/2)
	y = (screen_height/2) - (height/2)
	root.geometry("%dx%d+%d+%d" % (width, height, x, y))
	root.resizable(0, 0)


	USERNAME = IntVar()
	PASSWORD = StringVar()
	 

	Top = Frame(root, bd=2,  relief=RIDGE)
	Top.pack(side=TOP, fill=X)
	Form = Frame(root, height=200)
	Form.pack(side=TOP, pady=20)
	 

	lbl_title = Label(Top, text = "Kindly log in to continue", font=('arial', 15))
	lbl_title.pack(fill=X)
	lbl_username = Label(Form, text = "Unique ID:", font=('arial', 14), bd=15)
	lbl_username.grid(row=0, sticky="e")
	lbl_password = Label(Form, text = "Password:", font=('arial', 14), bd=15)
	lbl_password.grid(row=1, sticky="e")
	lbl_text = Label(Form)
	lbl_text.grid(row=2, columnspan=2)
	 

	username = Entry(Form, textvariable=USERNAME, font=(14))
	username.grid(row=0, column=1)
	password = Entry(Form, textvariable=PASSWORD, show="*", font=(14))
	password.grid(row=1, column=1)
	 

	btn_login = Button(Form, text="Login", width=45, command=Login)
	btn_login.grid(pady=25, row=3, columnspan=2)
	btn_login.bind('<Return>', Login)

	root.mainloop()

#LoginForm()