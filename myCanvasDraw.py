#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# разбираюсь самостоятельно в рисовании


from tkinter import *

class CanvasEventsDemo:
    def __init__(self, parent=None):
        canvas = Canvas(width=300, height=300, bg='blue')
        canvas.pack()
        canvas.bind('<ButtonPress-1>', self.onStart) # щелчок
        canvas.bind('<B1-Motion>', self.onGrow) # движение мыши с зажатой лкм
        self.canvas = canvas
        self.drawn = None
        self.size = 3

    def onStart(self, event):
        self.canvas.create_oval(event.x-self.size, event.y-self.size, event.x+self.size, event.y+self.size, fill='white')

    def onGrow(self, event):
        canvas = event.widget
        # if self.drawn: canvas.delete(self.drawn)
        objectId = self.canvas.create_oval(event.x, event.y, event.x, event.y)
        self.drawn = objectId

if __name__ == '__main__':
    CanvasEventsDemo()
    mainloop()
