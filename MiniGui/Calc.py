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

txtDisplay = Entry(cal, font=('arial', 20, 'bold'),  bd=40, textvariable=text_Input,insertwidth=5,
                   justify="right").grid(columnspan=5)
"#==========================================================================================================================#"

btn7 = Button(cal, padx=18, pady=18, fg="black", font=('arial', 20, 'bold'), text="7",command=btnclick(7)).grid(row=1, column=0)

btn8 = Button(cal, padx=18, pady=18, fg="black", font=('arial', 20, 'bold'), text="8",command=btnclick(6)).grid(row=1, column=1)


btn9 = Button(cal, padx=18, pady=18, fg="black", font=('arial', 20, 'bold'), text="9",command=btnclick(9)).grid(row=1, column=2)

add = Button(cal, padx=18, pady=18, fg="black", font=('arial', 20, 'bold'), text="+",command=btnclick('+')).grid(row=1, column=3)

""""""""""#===========================================================================================================================#"""""""""

btn4 = Button(cal, padx=18, pady=18, fg="black", font=('arial', 20, 'bold'), text="4",command=btnclick(4)).grid(row=2, column=0)

btn5 = Button(cal, padx=18, pady=18, fg="black", font=('arial', 20, 'bold'), text="5",command=btnclick(5)).grid(row=2, column=1)


btn6 = Button(cal, padx=18, pady=18, fg="black", font=('arial', 20, 'bold'), text="6",command=btnclick(6)).grid(row=2, column=2)

sub = Button(cal, padx=18, pady=18, fg="black", font=('arial', 20, 'bold'), text="-",command=btnclick('-')).grid(row=2, column=3)

""#========================================================================================================================#""

btn1 = Button(cal, padx=18, pady=18, fg="black", font=('arial', 20, 'bold'), text="1",command=btnclick(1)).grid(row=3, column=0)

btn2 = Button(cal, padx=18, pady=18, fg="black", font=('arial', 20, 'bold'), text="2",command=btnclick(2)).grid(row=3, column=1)


btn3 = Button(cal, padx=18, pady=18, fg="black", font=('arial', 20, 'bold'), text="3",command=btnclick(3)).grid(row=3, column=2)

mul = Button(cal, padx=18, pady=18, fg="black", font=('arial', 20, 'bold'), text="*",command=btnclick('*')).grid(row=3, column=3)

#========================================================================================================================#

btn0 = Button(cal, padx=18, pady=18, fg="black", font=('arial', 20, 'bold'), text="0",command=btnclick(0)).grid(row=4, column=0)

btnClear = Button(cal, padx=18, pady=18, fg="black", font=('arial', 20, 'bold'), text="c",command=btnClearDisplay).grid(row=4, column=1)


btnEquals = Button(cal, padx=18, pady=18, fg="black", font=('arial', 20, 'bold'), text="=",command=btnEqualsInput).grid(row=4, column=2)

div = Button(cal, padx=18, pady=18, fg="black", font=('arial', 20, 'bold'), text="/",command=btnclick('/')).grid(row=4, column=3)



cal.mainloop()
