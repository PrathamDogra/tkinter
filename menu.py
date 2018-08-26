from tkinter import *
root=Tk()
def random():
    print("you are at right place")

mainMenu=Menu(root)#definig menu
root.configure(menu= mainMenu)#we are setting our root menu to mainMenu

subMenu=Menu(mainMenu)#setting submenu 
mainMenu.add_cascade(label="file",menu=subMenu)#adding dropdown for the submenu from menu with name file 
#label=name the submenu, menu=here we assignig the drop down 
subMenu.add_command(label="rabdom function",command=random)
#addig  command to be performed 
#label=name to be displyed, command=function whcihhas to be called
subMenu.add_command(label="new file",)
subMenu.add_separator()#add  dash line seprator
subMenu.add_command(label="halloween",command=random)
subMenu2=Menu(mainMenu)
mainMenu.add_cascade(label="view",menu=subMenu2)
subMenu2.add_command(label="old",command=random)

root.mainloop()
