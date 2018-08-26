from tkinter import *
import random
import time

root=Tk()
root.title("Bounce")
root.resizable(0,0)#we cant resize window 
root.wm_attributes("-topmost",1)#its is to place our window top of all other window
canvas=Canvas(root,width=500,height=500,bd=0,highlightthickness=0)#bd=border,boredeer thickness
canvas.pack()

root.update()

#creating ball class
class Ball:
    def __init__(self,canvas,paddle,color):
        self.canvas=canvas
        self.paddle=paddle
        self.id=canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,245,300 )#move(from old ,to new position)
        start=[-3,-2,-1,0,1,2,3]
        random.shuffle(start)
        self.x=start[0]#object variable is set =0
        self.y=-3 
        self.canvas_height=self.canvas.winfo_height()#setting canvas geight equal to height of window
        self.canvas_width=self.canvas.winfo_width()
        self.hit_bottom=False

    def hit_paddle(self,pos):
        paddle_pos= self.canvas.coords(self.paddle.id)
        if pos[2]>=paddle_pos[0] and pos[0]<=paddle_pos[2]:
            if pos[3]>=paddle_pos[1] and pos[3]<=paddle_pos[3]:
                return True
            return False

        
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)#we are using self instead of canvas cause __init__ saved canvas paramter as object variable 
        #move(current position,xmovement,ymovement)
        pos= self.canvas.coords(self.id)#return an array of (x1,y1,x2.y2)
        print(pos)
        if pos[1]<=0:# it will reverse the movemnet of ball when it reach the top 1 refer y1
            self.y=3
        if pos[3]>=self.canvas_height:#when reach at max heightof window 3 refer y2
            self.hit_bottom=True
            canvas.create_text(250,250,text="GAME OVER")
        if pos[0]<=0:
            self.x=3
        if pos[2]>=self.canvas_width:
            self.x=-3
        if self.hit_paddle(pos)==True:
            self.y=-3
            
class Paddle:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id,200,300)
        self.x=0
        self.canvas_width=self.canvas.winfo_width()
        self.canvas.bind_all("<KeyPress-Left>",self.turn_left)
        self.canvas.bind_all("<KeyPress-Right>",self.turn_right)
    def draw(self):
        self.canvas.move(self.id,self.x,0)
        pos = self.canvas.coords(self.id)
        if pos[0]<=0:
            self.x= 0
        if pos[2]>=self.canvas_width:
            self.x= 0

    def turn_left(self,event):
        self.x=-2
    def turn_right(self,event):
        self.x=2

paddle=Paddle(canvas,"green")       
ball= Ball(canvas,paddle,'red')

while 1:
    ball.draw()
    paddle.draw()
    root.update_idletasks()#update background
    root.update()#updating foreground 
    time.sleep(0.01)




root.mainloop()
