from tkinter import *
root=Tk()

label1=Label(root,text="Name:",fg="red")
label1.grid(row=0,column=0,sticky="E")#it right alligne labelin the grid
entrySpace= Entry(root)#create input box
entrySpace.grid(row=0, column=1,sticky="E")#it take iput E W N S which are in general directions

label2=Label(root,text="Password:",fg="red")
label2.grid(row=3,column=0)
cbutton= Checkbutton(root,text="remeber password")#create checkbox
cbutton.grid(columnspan=2)
entrySpace2=Entry(root)
entrySpace2.grid(row=1,column=1)
root.mainloop()