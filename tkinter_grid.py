from tkinter import *

root=Tk()
#pack and grid same function but with different  approach

label1=Label(root,text="hey")
label2=Label(root,text="there !!!")
label3=Label(root,text="wassup")

label1.grid(row= 0, column=0)
label2.grid(row= 0, column=1)
label3.grid(row= 1, column=0)

root.mainloop()