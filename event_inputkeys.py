from tkinter import *
root=Tk()

def leftClick(event):
    print("left")

def rightclick(event):
    print("right")

def croll(event):
    print("scroll")

def leftKey(event):
    print("left key pressed")

def rightKey(event):
    print("right key is pressed")

root.geometry("1024x720")#it definex te size of root window

root.bind("<Button-1>",leftClick)
root.bind("<Button-2>",rightclick)
root.bind("<Button-3>",croll)
root.bind("<Left>",leftKey)
root.bind("<Right>",rightKey)

root.mainloop()
