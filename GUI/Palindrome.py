#Checks whether a string is a palindrome or not and displays the result

from tkinter import *

def is_pal():
	mystr=e1.get().upper()
	e2.place(x=20,y=200,height=60,width=200)
	if(mystr==mystr[::-1]):
		ans.set("{} is a Palindrome String !!!".format(mystr))
	else:
		ans.set("{} is NOT a Palindrome String.".format(mystr))

def forget():
	e2.place_forget()

def exit1():
	root.destroy()

root = Tk()
root.geometry('400x400')
root.title('Palindrome Checker')
root.resizable(width=False,height=False)
root.configure(background='ivory')

ans=StringVar()

l1=Label(root,text="Enter string: ",bg="ivory")
l1.place(x=20,y=30)

e1=Entry(root)
e1.place(x=100,y=30)

b1=Button(root,text="isPalindrome??",command=is_pal)
b1.place(x=20,y=100)

b2=Button(root,text="Reset",command=forget)
b2.place(x=140,y=100)

b3=Button(root,text="Exit",command=exit1)
b3.place(x=200,y=100)

e2=Entry(root,textvariable=ans)

root.mainloop()