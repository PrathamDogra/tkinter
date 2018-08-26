from tkinter import *
root=Tk()
equa=""#used to store all the variable 
equation=StringVar()#everytime we change our change strigvar our equation also change
calculation= Label(root,textvariabl=equation)

calculation.grid(columnspan=4)
def EqualPress():
    global equa
    total=str(eval(equa))
    equation.set(total)
    equa=""


def btnpress(num):
    global equa#global is used so that it can be used so that we can modify equa here
    equa=equa+str(num)
    equation.set(equa)

def ClearEq():
    global equa
    equa=""
    equation.set(equa)


#lamda is annomous fuction ,it have no return type
button1=Button(root,text="1",command=lambda:btnpress(1)) 
button1.grid(row=1,column=0)
button2=Button(root,text="2",command=lambda:btnpress(2)) 
button2.grid(row=1,column=1)
button1=Button(root,text="3",command=lambda:btnpress(3)) 
button1.grid(row=1,column=2)
button1=Button(root,text="4",command=lambda:btnpress(4)) 
button1.grid(row=2,column=0)
button1=Button(root,text="5",command=lambda:btnpress(5)) 
button1.grid(row=2,column=1)
button1=Button(root,text="6",command=lambda:btnpress(6)) 
button1.grid(row=2,column=2)
button1=Button(root,text="7",command=lambda:btnpress(7)) 
button1.grid(row=3,column=0)
button1=Button(root,text="8",command=lambda:btnpress(8)) 
button1.grid(row=3,column=1)
button1=Button(root,text="9",command=lambda:btnpress(9)) 
button1.grid(row=3,column=2)
button0=Button(root,text="0",command=lambda:btnpress(0))
button0.grid(row=4,column=2)
add=Button(root,text="+",command=lambda:btnpress("+"))
add.grid(row=1,column=3)
add.configure(width=10,height=15)

minus=Button(root,text="-",command=lambda:btnpress("-"))
minus.grid(row=2,column=3)
multi=Button(root,text="*",command=lambda:btnpress("*"))
multi.grid(row=3,column=3)
divide=Button(root, text="/",command=lambda:btnpress("/"))
divide.grid(row=4,column=3)
equal=Button(root,text="=",command=lambda:EqualPress())
equal.grid(row=4,column=0)
clear=Button(root,text="C",command=lambda:ClearEq())
clear.grid(row=4,column=1)
root.mainloop
