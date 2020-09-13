from tkinter import *
import tkinter.messagebox
root=Tk()

def cquit():
    answer=tkinter.messagebox.askokcancel("Are you sure?","All the unsaved changes ill be lost!!")
    if answer:
        print("Qiting")
        quit()

m1=Menu(root)
root.config(menu=m1)

sm1=Menu(m1)
m1.add_cascade(label="File",menu=sm1)
sm1.add_cascade(label="New")
sm1.add_cascade(label="Old")
sm1.add_cascade(label="Bad Luck")
sm1.add_command(label="Exit",command=cquit)

sm2=Menu(m1)
m1.add_cascade(label="HElp",menu=sm2)
sm2.add_cascade(label="Grey")
sm2.add_cascade(label="Hey there !!")
sm2.add_cascade(label="Your Luck( h ah ah a h hah a) ")

root.mainloop()