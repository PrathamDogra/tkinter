from tkinter import *
import random
root=Tk()
canvas=Canvas(root,width=500,height=500)
canvas.pack()
col=""
color=["red","gold","green","blue","voilet"]
def randomRect(num):#here num is the numberof rectangle to be created
    for i in range(0,num):
        global col=random.shuffle(color)
        x1=random.randrange(300)#randrange is the function of Random library with which we will create randow co ordinates for rect.
        y1=random.randrange(300)
        x2=x1+random.randrange(300)
        y2=y1+random.randrange(300)
        canvas.create_rectangle(x1,y1,x2,y2,fill=col)
           

randomRect(400)


root.mainloop()
