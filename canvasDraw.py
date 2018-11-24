#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by Ivar at 24.11.2018

"""реализует возможность рисования эластичных фигур на холсте при перемещении
указателя мыши с нажатой правой кнопкой; версии этого сценария, дополненные
тегами и анимацией, вы найдете в файлах canvasDraw_tags*.py"""

from tkinter import *
trace = False

class CanvasEventsDemo:
    def __init__(self, parent=None):
        canvas = Canvas(width=300, height=300, bg='beige')
        canvas.pack()
        canvas.bind('<ButtonPress-1>', self.onStart) # щелчок
        canvas.bind('<B1-Motion>', self.onGrow) # и вытягивание
        canvas.bind('<Double-1>', self.onClear) # удалить все
        canvas.bind('<ButtonPress-3>', self.onMove) # перемещать последнюю
        self.canvas = canvas
        self.drawn = None
        self.kinds = [canvas.create_oval, canvas.create_rectangle]

    def onStart(self, event):
        self.shape = self.kinds[0]
        self.kinds = self.kinds[1:] + self.kinds[:1]  # начало вытягивания
        self.start = event
        self.drawn = None

    def onGrow(self, event):  # удалить и перерисовать
        canvas = event.widget
        if self.drawn: canvas.delete(self.drawn)
        objectId = self.shape(self.start.x, self.start.y, event.x, event.y)
        if trace: print(objectId)
        self.drawn = objectId

    def onClear(self, event):
        event.widget.delete('all')  # использовать тег all

    def onMove(self, event):
        if self.drawn:  # передвинуть в позицию
            if trace: print(self.drawn)  # щелчка
            canvas = event.widget
            diffX, diffY = (event.x - self.start.x), (event.y - self.start.y)
            canvas.move(self.drawn, diffX, diffY)
            self.start = event

if __name__ == '__main__':
    CanvasEventsDemo()
    mainloop()