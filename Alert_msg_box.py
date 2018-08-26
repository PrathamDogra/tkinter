from tkinter import *
import tkinter.messagebox
root=Tk()
#showinfo display information
#there are various type of messagesbox
tkinter.messagebox.showinfo("title","did you know that world just blew up")
#messagebox(title,  message to be displayed) 
ans=tkinter.messagebox.askquestion("Question Box","are you an idiot?")

if ans=="yes":
    tkinter.messagebox.showinfo("","you are dumb")
else:
    tkinter.messagebox.showinfo("","you are awesome")



root.mainloop()
