from tkinter import *
import time
root= Tk()
canvas= Canvas(root,width=500,height=300)
canvas.pack()
canvas.create_polygon(10,10,10,60,50,35)
def PressKey(event):
    canvas.move(1,10,0)#1 specify polygon,x amounnt move,yamount move
    root.update()#update screen or window

root.bind("<Return>",PressKey)
root.mainloop()