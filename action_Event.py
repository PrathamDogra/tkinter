from tkinter import *
master=Tk()

def printName(event):#work when a event take place like clicking 
    print("vikesh")

label1=Label(master,text="name")
label1.pack()
entrySpace=Entry(master)
entrySpace.pack()
button1= Button(master,text="print")
button1.bind("<Button-1>",printName)#<Button-1> is te key bind coode for the lests mouse button ,which act as te event input,next to it is the function that has to be performed when the event occurs.
button1.pack()

master.mainloop()