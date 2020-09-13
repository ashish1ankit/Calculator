from tkinter import *
root=Tk()
def Frist():
    print("Fiel contains .......")
root.geometry("600x400")
def save():
    print("no file to save!!")
def touch():
    print("If You Dont Know , Dont Touch It!!")
def know():
    print("Seriously!!")
    print("How could you just Know The Thing!!")
    print("Just Know!!  and What it Means ""EXACTLY""")
def leave():
    print("No!\n You Do your work!!No Time To LEave!!")
def seti():
    print("Damn boy Thier is no setting avilable!!")
#size changing functions
def smal():
    print("Smaller Window")
    root.geometry("400x200")#changing the size
def nor():
    print("Normal Window")
    root.geometry("600x400")
def big():
    print("Bigger Window")
    root.geometry("900x900")

m1=Menu(root)
root.config(menu=m1)

#first menu
sm1=Menu(m1)
m1.add_cascade(label="File",menu=sm1)
sm1.add_cascade(label="New")
sm1.add_cascade(label="Open")
#sub save menu
smm1=Menu(sm1)
sm1.add_cascade(label="Save",menu=smm1)
smm1.add_cascade(label="Save As")
smm1.add_command(label="Save",command=save)
#normal sub menu
sm1.add_cascade(label="Setting")
sm1.add_command(label="Exit",command=quit)


#second menu
sm2=Menu(m1)
m1.add_cascade(label="Edit",menu=sm2)
sm2.add_cascade(label="Undo")
sm2.add_cascade(label="Cut")
sm2.add_command(label="Copy",command=save)
sm2.add_cascade(label="Paste")
sm2.add_cascade(label="Find")

sm3=Menu(m1)
m1.add_cascade(label="View",menu=sm3)
sm3.add_cascade(label="Tools")
sm3.add_cascade(label="Recent Files")
sm3.add_command(label="Tool Bars",command=save)
sm3.add_cascade(label="Setting")

sm4=Menu(m1)
m1.add_cascade(label="Code",menu=sm4)
sm4.add_cascade(label="Surround")
sm4.add_cascade(label="Insert")
sm4.add_command(label="Move",command=save)
sm4.add_cascade(label="Collaborate")

sm5=Menu(m1)
m1.add_cascade(label="Run",menu=sm5)
sm5.add_cascade(label="New")
sm5.add_cascade(label="Open")
sm5.add_command(label="Small Window",command=smal)
sm5.add_command(label="Normal Window",command=nor)
sm5.add_command(label="Extended Window",command=big)
sm5.add_command(label="Exit",command=quit)

sm6=Menu(m1)
m1.add_cascade(label="Help",menu=sm6)
sm6.add_command(label="I dont know the thing",command=touch)
sm6.add_command(label="Know the thing but dont know how to use it",command=know)
sm6.add_command(label="Just leave me",command=leave)
sm6.add_command(label="Setting",command=seti)
sm6.add_command(label="I want to quit",command=quit)

s1=Label(root,text="Running........",anchor=W,relief=SUNKEN,bd=1)
s1.pack(side=BOTTOM,fill=X)

root.mainloop()