from tkinter import *

win=Tk()
win.title("Calculator")
win.configure(bg="white")

e=Entry(win,bg="light blue",width=35,borderwidth=5,relief=SUNKEN)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
# e.insert(0,"Enter your number.")

def button_actions(number):
    # e.delete(0, END)
    current_num=e.get()
    e.delete(0, END)
    e.insert(0, str(current_num) + str(number))

def button_clear():
    e.delete(0, END)

def button_equal():
    second_number=e.get()
    e.delete(0, END)
    
    if math=="addition":
        e.insert(0, f_number+int(second_number))
    elif math=="substraction":
        e.insert(0, f_number-int(second_number))
    elif math=="multiplication":
        e.insert(0, f_number*int(second_number))
    elif math=="division":
        e.insert(0, f_number/int(second_number))
    else:
        e.insert(0, "This wasn't suppose to happen.")


def button_sub():
    first_number=e.get()
    global f_number
    f_number=int(first_number)
    global math
    math="substraction"
    e.delete(0, END)

def button_multiply():
    first_number=e.get()
    global f_number
    f_number=int(first_number)
    global math
    math="multiplication"
    e.delete(0, END)

def button_division():
    first_number=e.get()
    global f_number
    f_number=int(first_number)
    global math
    math="division"
    e.delete(0, END)

#Clear Button
Button1=Button(win,text="Clear",width=10,borderwidth=3,height=3,background="white",relief=SUNKEN,command=lambda: button_clear())

#Just Numbers
Button_1=Button(win,text="1",width=10,borderwidth=3,height=3,background="white",relief=SUNKEN,command=lambda: button_actions(1))
Button_2=Button(win,text="2",width=10,borderwidth=3,height=3,background="white",relief=SUNKEN,command=lambda: button_actions(2))
Button_3=Button(win,text="3",width=10,borderwidth=3,height=3,background="white",relief=SUNKEN,command=lambda: button_actions(3))
Button_4=Button(win,text="4",width=10,borderwidth=3,height=3,background="white",relief=SUNKEN,command=lambda: button_actions(4))
Button_5=Button(win,text="5",width=10,borderwidth=3,height=3,background="white",relief=SUNKEN,command=lambda: button_actions(5))
Button_6=Button(win,text="6",width=10,borderwidth=3,height=3,background="white",relief=SUNKEN,command=lambda: button_actions(6))
Button_7=Button(win,text="7",width=10,borderwidth=3,height=3,background="white",relief=SUNKEN,command=lambda: button_actions(7))
Button_8=Button(win,text="8",width=10,borderwidth=3,height=3,background="white",relief=SUNKEN,command=lambda: button_actions(8))
Button_9=Button(win,text="9",width=10,borderwidth=3,height=3,background="white",relief=SUNKEN,command=lambda: button_actions(9))
Button_10=Button(win,text="0",width=10,borderwidth=3,background="white",height=3,relief=SUNKEN,command=lambda: button_actions(0))

#Action Buttons
Button_11=Button(win,text="=",width=10,borderwidth=3,height=3,bg="purple",fg="white",relief=SUNKEN,command=lambda: button_equal())
Button_13=Button(win,text="-",width=10,borderwidth=3,background="grey",fg="white",height=3,relief=SUNKEN,command=lambda: button_sub())
Button_14=Button(win,text="*",width=10,borderwidth=3,background="grey",fg="white",height=3,relief=SUNKEN,command=lambda: button_multiply())
Button_15=Button(win,text="/",width=10,borderwidth=3,background="grey",fg="white",height=3,relief=SUNKEN,command=lambda: button_division())

#Positioning The Buttons
Button1.grid(row=0,column=3)
Button_1.grid(row=1,column=0)
Button_2.grid(row=1,column=1)
Button_3.grid(row=1,column=2)

Button_4.grid(row=2,column=0)
Button_5.grid(row=2,column=1)
Button_6.grid(row=2,column=2)

Button_7.grid(row=3,column=0)
Button_8.grid(row=3,column=1)
Button_9.grid(row=3,column=2)

Button_10.grid(row=4,column=0)
Button_11.grid(row=4,column=1)
Button1.grid(row=4,column=2)

Button_13.grid(row=5,column=0)
Button_14.grid(row=5,column=1)
Button_15.grid(row=5,column=2)

win.mainloop()
