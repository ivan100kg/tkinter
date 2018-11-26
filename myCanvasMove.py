# будем перемещаться по холсту

from tkinter import *
import time
import math

class App():
    def __init__(self, parent=None):
        width = 640
        height = 480
        self.pX = width/2
        self.pY = height/2

        canvas = Canvas(parent, width=width, height=height, background='brown')
        canvas.pack()
        canvas.focus_set()
        pers = canvas.create_rectangle(self.pX-8,self.pY-16,self.pX+8,self.pY+16,fill='white', tag='pers')

        canvas.create_rectangle(-100,-100,0,0, fill='black', tag='world')
        canvas.create_rectangle(-200,-200,-150,-150, fill='black', tag='world')
        canvas.create_rectangle(-300,-300,-250,-250, fill='black', tag='world')
        canvas.create_rectangle(400,300,500,350, fill='black', tag='world')
        canvas.create_rectangle(700,400,800,600, fill='black', tag='world')
        canvas.create_rectangle(800,500,1200,550, fill='black')
        canvas.bind('<Up>', lambda event: canvas.move('world', 0,1))
        canvas.bind('<Down>', lambda event: canvas.move('world', 0,-1))
        canvas.bind('<Left>', lambda event: canvas.move('world', 1,0))
        canvas.bind('<Right>', lambda event: canvas.move('world', -1,0))
        canvas.bind('<ButtonPress-1>', self.moveTo)
        self.canvas = canvas

    def moveTo(self, event):
        self.stepX = 0  # обнуляем, для того чтобы при
        self.stepY = 0  # новом нажатии старые команды отменились 
        x = event.x     # координаты нажатия мыши
        y = event.y

        print(self.pX, self.pY,x,y)

        
        # расчет катетов гипотенузы и угла
        AC = max(self.pX, x) - min(self.pX, x)  # прил катет
        BC = max(self.pY, y) - min(self.pY, y)  # противоположный катет рабочий
        AB = pow((AC**2 + BC**2), 0.5)  # гипотенуза
        sinA = BC/AB   # синус угла
        cosA = AC/AB   # косинус угла
        print("AC = {}, BC = {}, AB = {}".format(AC,BC,AB))

        ab = 2  # шаг, или мини гипотенуза, или отрезок за тик
        self.stepX = cosA*ab    # рассчет перемещения экрана по x y 
        self.stepY = sinA*ab
        print(self.stepX*AB, self.stepY*AB)
        # направление движения, вычитать или прибавлять шаг   
        if x > self.pX: self.stepX *= -1
        elif x < self.pX: self.stepX *= 1
        elif x == self.pX: self.stepX = 0
        if y > self.pY: self.stepY *= -1
        elif y < self.pY: self.stepY *= 1
        elif y == self.pY: self.stepY = 0
        
        done = True
        while done: 
            self.canvas.move('world', self.stepX, self.stepY)   # движение тега world
            # остановка экрана когда достигнута точка нажатия
            if self.stepX < 0:
                if x <= self.pX: self.stepX = 0
            if self.stepX > 0:
                if x >= self.pX: self.stepX = 0
            if self.stepY < 0:
                if y <= self.pY: self.stepY = 0
            if self.stepY > 0:
                if y >= self.pY: self.stepY = 0
            if self.stepX == 0 and self.stepY == 0: # условие выхода из цикла
                break        
            x += self.stepX         # движение экрана
            y += self.stepY
            time.sleep(1/60)        # fps
            self.canvas.update()    # отрисовка
            




if __name__ == '__main__':
    root = Tk()
    root.title('moving')
    App(root)
    root.mainloop()
