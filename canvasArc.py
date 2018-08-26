from tkinter import *
root =Tk()
canvas=Canvas(root,width=300,height=300)
canvas.pack()
canvas.create_arc(10,10,200,60,extent=359,style=ARC)#first two are the sarting pont  of box in which acr will be drawn and other two are ending pt.


root.mainloop()
