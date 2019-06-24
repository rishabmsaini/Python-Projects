from tkinter import *
from tkinter import filedialog

class TextEditor:
    clip=" "
    filename=" "
    def __init__(self,root):
        filename="Untitled.txt"
        self.t=Text(root, width=80, height=20, wrap=WORD)
        self.t.pack()

#BASIC BODY:-
        self.menubar=Menu(root) #Creates a menubar

        root.config(menu=self.menubar) #Attach menubar to root window, same as pack

    #FILE SECTION:-
        self.filemenu=Menu(root,tearoff=0) #Create file menu

        #create menu items in file menu
        self.filemenu.add_command(label="New",command=self.new_file)

        self.filemenu.add_command(label="Open File",command=self.open_file)

        self.filemenu.add_separator() #Add a horizontal seperator

        self.filemenu.add_command(label="Save",command=self.save_file)
        self.filemenu.add_command(label="Save As...",command=self.saveas_file)

        self.filemenu.add_separator() #Add
        self.filemenu.add_command(label="Exit",command=root.destroy) #Another menu item under seperator

        #Add file menu with name "File" to the menubar
        self.menubar.add_cascade(label="File", menu=self.filemenu)

    #EDIT SECTION:-
        self.editmenu=Menu(root,tearoff=0)

        self.editmenu.add_command(label="Cut",command=self.cut)
        self.editmenu.add_command(label="Copy",command=self.copy)
        self.editmenu.add_command(label="Paste",command=self.paste)

        self.menubar.add_cascade(label="Edit", menu=self.editmenu)

#MAIN CODE:-

    #def donothing(self):
    #   pass

    def new_file(self):
        self.t.delete(1.0,END)

    def save_file(self):
        if(self.filename=='Untitled.txt'):
            self.saveas_file()
        else:
            s=self.t.get(0.0,END)
            f=open(self.filename,'w')
            f.write(s)
            f.close()

    #Method for opening file and displaying it's content in the text box
    def open_file(self):
        self.filename=filedialog.askopenfilename(parent=root, title="Select a file",filetypes=( ("All Files","*.*"), ("C Files","*.c"), ("Java Files","*.java"), ("C++ Files","*.cpp"), ("Python Files","*.py") ) )
        if(self.filename!=None):
            self.t.delete(1.0,END)
            f=open(self.filename,'r')
            contents=f.read()
            self.t.insert(1.0,contents)
            f.close()

    #Method to save file that already exists in the text box
    def saveas_file(self):
        self.filename=filedialog.asksaveasfilename(parent=root, title="Save the file", defaultextension=".txt")
        if(self.filename!=None):
            f=open(self.filename,'w')
            contents=str(self.t.get(1.0,END))
            f.write(contents)
            f.close()

    #Edit code
    def copy(self):
        self.clip = self.t.get(SEL_FIRST,SEL_LAST)

    def cut(self):
        self.clip = self.t.get(SEL_FIRST,SEL_LAST)
        self.t.delete(SEL_FIRST,SEL_LAST)

    def paste(self):
        i=self.t.index(INSERT)
        self.t.insert(i,self.clip)

root=Tk() #Creates a blank window.

root.title("TEXT EDITOR")
root.geometry("500x300")
root.wm_iconbitmap('R.ico')

obj=TextEditor(root)

root.mainloop() #Doesn't let the program close after exeuting all stmnts until "x" is clicked.
