from tkinter import*

def  btnclick(number):
    global operator
    operator = operator + str(number)
    text_Input.set(operator)


def btnClearDisplay():
    global operator
    operator = ""
    text_Input.set("")


def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)


cal = Tk()
cal.title("calculator")
operator = ""
text_Input = StringVar()

txtDisplay = Entry(cal, font=('arial', 20, 'bold'), textvariable=text_Input, bd=40, insertwidth=5,
                   justify="right").grid(columnspan=5)
"#==========================================================================================================================#"

btn7 = Button(cal, padx=18, pady=18, fg="black", font=('arial', 20, 'bold'), text="7", command=lambda: btnclick(7)).grid(row=1, column=0)

btn8 = Button(cal, padx=18, pady=18, fg="black", font=('arial', 20, 'bold'), text="8", command=lambda:btnclick(8)).grid(row=1, column=1)


btn9 = Button(cal, padx=18, pady=18, fg="black", font=('arial', 20, 'bold'), text="9", command=lambda:btnclick(9)).grid(row=1, column=2)

add = Button(cal, padx=18, pady=18, fg="black", font=('arial', 20, 'bold'), text="+",  command=lambda:btnclick("+")).grid(row=1, column=4)

""""""""""#===========================================================================================================================#"""""""""

btn4 = Button(cal, padx=18, pady=18, fg="black", font=('arial', 20, 'bold'), text="7", command=lambda:btnclick(4)).grid(row=1, column=0)

btn5 = Button(cal, padx=18, pady=18, fg="black", font=('arial', 20, 'bold'), text="8", command=lambda:btnclick(5)).grid(row=1, column=1)


btn6 = Button(cal, padx=18, pady=18, fg="black", font=('arial', 20, 'bold'), text="9", command=lambda:btnclick(6)).grid(row=1, column=2)

sub = Button(cal, padx=18, pady=18, fg="black", font=('arial', 20, 'bold'), text="-",  command=lambda:btnclick("-")).grid(row=1, column=4)

""#========================================================================================================================#""

btn1 = Button(cal, padx=18, pady=18, fg="black", font=('arial', 20, 'bold'), text="7", command=lambda:btnclick(1)).grid(row=1, column=0)

btn2 = Button(cal, padx=18, pady=18, fg="black", font=('arial', 20, 'bold'), text="8", command=lambda:btnclick(2)).grid(row=1, column=1)


btn3 = Button(cal, padx=18, pady=18, fg="black", font=('arial', 20, 'bold'), text="9", command=lambda:btnclick(3)).grid(row=1, column=2)

mul = Button(cal, padx=18, pady=18, fg="black", font=('arial', 20, 'bold'), text="+", command=lambda:btnclick("*")).grid(row=1, column=4)

#========================================================================================================================#

btn0 = Button(cal, padx=18, pady=18, fg="black", font=('arial', 20, 'bold'), text="0", command=lambda:btnclick(0)).grid(row=1, column=0)

btnClear = Button(cal, padx=18, pady=18, fg="black", font=('arial', 20, 'bold'), text="c", command=lambda:btnclick("c")).grid(row=1, column=1)


btnEquals = Button(cal, padx=18, pady=18, fg="black", font=('arial', 20, 'bold'), text="=", command=lambda:btnclick("=")).grid(row=1, column=2)

div = Button(cal, padx=18, pady=18, fg="black", font=('arial', 20, 'bold'), text="+", command=lambda:btnclick("/")).grid(row=1, column=4)



cal.mainloop()
