from tkinter import *
root =Tk()

lab=Label(root,text="enter your expression:")
lab.pack()
def evaluate(event):
    data=gg.get()#store entry into variabe data with the help of get function
    ans.configure(text="Answer:"+str(eval(data)))#str convert the evaluated data  


gg=Entry(root)#take entry from user
gg.bind("<Return   >",evaluate)#with bind everytime we have to give bind parameter
gg.pack()
ans=Label(root)
ans.pack()

root.mainloop()