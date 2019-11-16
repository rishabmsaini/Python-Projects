from tkinter import *
import pymysql

def UpdateValues():
	def Update():
		UNID = int(unid.get())
		data1 = int(e1.get())
		data2 = int(e2.get())
		data3 = e3.get()

		conn= pymysql.connect(host='localhost',user='root',password='WeRock',db='foodchainmanagement',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
		cur = conn.cursor()
		cur.execute("UPDATE FARMER SET Weight_per_yeild=%d, Cost_per_quintal=%d, Mobile='%s' WHERE Unid=%d" % (data1, data2, data3,UNID))
		print("VALUES UPDATED SUCCESSFULLY")
		conn.commit()
		conn.close()
		root.destroy()


	root = Tk()
	root.geometry("400x400")
	root.title("Update Values")

	label_0 = Label(root, text="ENTER UNID:",width=20,font=("bold", 10))
	label_0.place(x=70,y=50)

	unid = IntVar()
	unid = Entry(root, textvariable=unid)
	unid.place(x=240,y=50)


	label_1 = Label(root, text="Weight per yeild:",width=20,font=("bold", 10))
	label_1.place(x=70,y=130)

	wpy = IntVar()
	e1 = Entry(root, textvariable=wpy)
	e1.place(x=240,y=130)

	label_2 = Label(root, text="Cost per quintal:",width=20,font=("bold", 10))
	label_2.place(x=70,y=180)

	cpq = IntVar()
	e2 = Entry(root, textvariable=cpq)
	e2.place(x=240,y=180)

	label_3 = Label(root, text="Mobile no.:",width=20,font=("bold", 10))
	label_3.place(x=70,y=230)

	mobile = StringVar()
	e3 = Entry(root, textvariable=mobile)
	e3.place(x=240,y=230)

	b2 = Button(root, text="EDIT PARTICULAR DATA", command=Update)
	b2.pack(side=BOTTOM)

	root.mainloop()

#UpdateValues()