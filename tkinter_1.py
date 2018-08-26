from tkinter import *#import every function availabel in tkinter
root= Tk()#defining a window

#creatig text 
theLabel = Label(root,text="this is my tkinter")#widget is defined 
theLabel.pack()#to pack thw widget with root or window
#always widget is defined first then it is packed with the root or window screen
theLabel2 = Label(root,text="this is second statment")
theLabel2.pack()

#creating button
theButton= Button(None,text="hit me",fg="green")#(button type, text , color)
theButton.pack()
ttheButton= Button(None,text="hit me",fg="blue")
ttheButton.pack()



root.mainloop()#to hold the window from dissapering
