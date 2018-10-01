from tkinter import *
master=Tk()

def printName():
    print("vikesh")

label1=Label(master,text="name")
label1.pack()
entrySpace=Entry(master)
entrySpace.pack()
button1= Button(master,text="print",command=printName,fg="red",bg="blue")#command usually perform action everytime button is clicked
button1.pack() 

master.mainloop()
