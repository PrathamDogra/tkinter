from tkinter import *
root=Tk()
canvas=Canvas(root,width=300,height=300)

canvas.pack()
canvas.create_rectangle(0,0,70,50)

def createRect(x1,y1,x2,y2):
    canvas.create_rectangle(x1,y1,x2,y2,fill="red")

createRect(20,30,10,10)
root.mainloop()
