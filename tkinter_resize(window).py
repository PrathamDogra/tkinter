from tkinter import *
root=Tk()
 
button1= Button(None,text="fist",fg="red",bg="green")#fg=foreground color, bg=backgroud color
button1.pack()
button2= Button(None,text="purple",fg="purple",bg="black")
button2.pack(fill=X)#it will completly x axis
button3=Button(None, text="Smash",fg="green",bg="blue")
button3.pack(side=RIGHT, fill=Y)#it will completly fill y axis
button4=Button(None,text="energy",fg="yellow",bg="orange")
button4.pack()

root.mainloop()