from tkinter import *
root=Tk()
root.geometry("366x266")
l1=Label(root,text="First enter the email id:")
l1.grid(row=0,sticky="e")
l2=Label(root,text="then enter the password:")
l2.grid(row=1)
e1=Entry(root)
e1.grid(row=0,column=1)
e2=Entry(root)
e2.grid(row=1,column=1)
c1=Checkbutton(root,text="Remember for future")
c1.grid(row=2,column=1)
b1=Button(root,text="submit")
b1.grid(row=3)
root.mainloop()