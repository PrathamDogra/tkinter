from tkinter import *
import time
root= Tk()
canvas= Canvas(root,width=500,height=300)
canvas.pack()
canvas.create_polygon(10,10,10,60,50,35)
for i in range(0,60):
    canvas.move(1,5,5)#1 specify polygon,x amounnt move,yamount move
    root.update()#update screen or window
    time.sleep(.01)#stop for .1 sec

root.mainloop()

