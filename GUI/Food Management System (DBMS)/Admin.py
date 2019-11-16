from tkinter import *
import pymysql.cursors

def Login():
	if(str(password.get())=="qwerty"):
		unid=int(entry_2.get())
		variable=str(var.get())
		conn= pymysql.connect(host='localhost',user='root',password='WeRock',db='foodchainmanagement',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
		cur = conn.cursor()
		cur.execute("DELETE FROM %s WHERE Unid=%d" % (variable,unid))
		print("VALUES DELETED SUCCESSFULLY")
		conn.commit()
		conn.close()
		root.destroy()

root = Tk()
root.geometry("700x400")
root.title("Admin's Portal")

label_0 = Label(root, text="ADMIN's PANEL",width=20,font=("bold", 20))
label_0.place(x=150,y=50)


label_1 = Label(root, text="Password:",width=20,font=('arial', 14), bd=15)
label_1.place(x=80,y=130)

password=StringVar()
unid=IntVar()
var=StringVar(root)

entry_1 = Entry(root,textvar=password,show="*",font=('arial', 14), bd=15)
entry_1.place(x=300,y=130)

label_2 = Label(root, text="Unid:",width=20,font=("bold", 10))
label_2.place(x=150,y=180)

entry_2 = Entry(root,textvar=unid,font=("bold", 10))
entry_2.place(x=300,y=180)

var.set("Select Role")
option_1=OptionMenu(root, var, "Farmer", "Distributor", "Retailer")
option_1.place(x=160,y=230)

btn_login = Button(root, text="Delete Data", width=45, command=Login)
btn_login.place(x=160,y=280)
btn_login.bind('<Return>', Login)

root.mainloop()