#step1: importing
from tkinter import *

#step2: gui interaction 
window=Tk()
window.geometry('500x500')  #set size of x=500 and y=500 
window.title("Calculator using TKINTER")
label=Label(text="You can do operations using this Calculator!!", font=(("Times New Roman"), 20, "bold"))
label.place(x=20, y=30)
#step3: adding inputs
#entry box 
e=Entry(width=50,borderwidth=3)
e.place(x=0, y=0)

def click(num):
    result=e.get()
    e.delete(0, END)
    e.insert(0, str(result) + str(num))

#buttons
btn=Button(text='1', width=12, command=lambda:click(1))
btn.place(x=1, y=60)

btn=Button(text='2', width=12, command=lambda:click(2))
btn.place(x=150, y=60)

btn=Button(text='3', width=12, command=lambda:click(3))
btn.place(x=300, y=60)

btn=Button(text='4', width=12, command=lambda:click(4))
btn.place(x=1, y=120)

btn=Button(text='5', width=12, command=lambda:click(5))
btn.place(x=150, y=120)

btn=Button(text='6', width=12, command=lambda:click(6))
btn.place(x=300, y=120)

btn=Button(text='7', width=12, command=lambda:click(7))
btn.place(x=1, y=180)

btn=Button(text='8', width=12, command=lambda:click(8))
btn.place(x=150, y=180)

btn=Button(text='9', width=12, command=lambda:click(9))
btn.place(x=300, y=180)

btn=Button(text='0', width=12, command=lambda:click(0))
btn.place(x=1, y=240)

def Add():
    n1=e.get()
    global math
    math= "Addition"
    global i
    i=int(n1)
    e.delete(0, END)

btn=Button(text='+', width=12, command=Add)
btn.place(x=150, y=240)

def Sub():
    n1=e.get()
    global math
    math= "Subtraction"
    global i
    i=int(n1)
    e.delete(0, END)

btn=Button(text='-', width=12, command=Sub)
btn.place(x=300, y=240)

def Multi():
    n1=e.get()
    global math
    math= "Multiplication"
    global i
    i=int(n1)
    e.delete(0, END)

btn=Button(text='*', width=12, command=Multi)
btn.place(x=1, y=300)

def Div():
    n1=e.get()
    global math
    math= "Division"
    global i
    i=int(n1)
    e.delete(0, END)

btn=Button(text='/', width=12, command=Div)
btn.place(x=150, y=300)

def equal():
    n2=e.get()
    e.delete(0, END)

    if math == "Addition":
        e.insert(0, i + int(n2))
    elif math == "Subtraction":
        e.insert(0, i - int(n2))
    elif math == "Multiplication":
        e.insert(0, i * int(n2))
    elif math == "Division":
        e.insert(0, i / int(n2))
btn=Button(text='=', width=12, command=equal)
btn.place(x=300, y=300)

def clear():
    e.delete(0, END)
btn=Button(text='clear', width=12, command=clear)
btn.place(x=150, y=350)

window.mainloop()