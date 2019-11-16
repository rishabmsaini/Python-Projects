from tkinter import *
import pymysql.cursors
from tkinter import ttk

def FarmerView():
	def PL():
		conn = pymysql.connect(host='localhost',user='root',password='WeRock',db='foodchainmanagement',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
		try:
			with conn.cursor() as cursor:
				sql = "SELECT Name,Mobile,State,City,Pincode,Capacity,Cost_per_quintal FROM Distributor"
				cursor.execute(sql)
				rows=cursor.fetchall()
				for row in rows:
					print(row)
					tree.insert("",END,values=(row["Name"],row["Mobile"],row["State"],row["City"],row["Pincode"],row["Capacity"],row["Cost_per_quintal"]))
		finally:
			conn.close()

	FView = Tk()
	FView.geometry("740x300")

	tree= ttk.Treeview(FView, selectmode="extended", column=("Name", "","Mobile", "State","City","Pincode","Capacity","Cost_per_quintal"), show='headings')
	
	tree.heading("#1", text="NAME")
	tree.column("#1",minwidth=0,width=120)
	tree.heading("#2", text="MOBILE")
	tree.column("#2",minwidth=0,width=100)
	tree.heading("#3", text="STATE")
	tree.column("#3",minwidth=0,width=100)
	tree.heading("#4", text="CITY")
	tree.column("#4",minwidth=0,width=100)
	tree.heading("#5", text="PINCODE")
	tree.column("#5",minwidth=0,width=100)
	tree.heading("#6", text="CAPACITY")
	tree.column("#6",minwidth=0,width=100)
	tree.heading("#7", text="COST PER QUINTAL")
	tree.column("#7",minwidth=0,width=120)

	tree.pack(fill=BOTH)

	b2 = Button(FView, text="View Data", command=PL)
	b2.place(x=350,y=250)

	FView.mainloop()

#FarmerView()