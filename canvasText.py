from tkinter import *
root =Tk()
canvas=Canvas(root,width=300,height=300)
canvas.pack()
canvas.create_text(150,150,text="you are awesome",fill="green",font=s("times", 30))#it is the coordinate of the text (middle)
#font style and than the size of the font

root.mainloop()
