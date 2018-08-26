from tkinter import *#import every function availabel in tkinter
root= Tk()#defining a window


#creating Frame
topFrame= Frame(root)
topFrame.pack()

botFrame= Frame(root)
botFrame.pack(side= BOTTOM)  


#craeting button
theButton= Button(topFrame,text="hit me",fg="green")#(button type, text , color)
theButton.pack(side= LEFT)
ttheButton= Button(topFrame,text="hit me",fg="blue")
ttheButton.pack(side= LEFT)
bButton= Button(botFrame,text="third",fg="red")
bButton.pack(side=LEFT)
btButton= Button(botFrame,text="forth",fg="yellow")
btButton.pack(side=LEFT)
root.mainloop()