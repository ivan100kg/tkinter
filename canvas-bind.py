# привязка обработчиков событий к холсту и к элементам на нем

from tkinter import *

def onCanvasClick(event):
    print('lot canvas click', event.x, event.y, event.widget)

def onObjectClick(event):
    print('Got object click', event.x, event.y, event.widget, end=' ')
    print(event.widget.find_closest(event.x, event.y))  # найти ID текстового
                                                        # объекта
root = Tk()
canv = Canvas(root, width=100, height=100)
obj1 = canv.create_text(50, 30, text='Click me one')
obj2 = canv.create_text(50, 70, text='Click me two')
canv.bind('<Double-1>', onCanvasClick)  # привязка к холсту
canv.bind(obj1, '<Double-1>', onObjectClick)    # привязка к объекту
canv.tag_bind(obj2, '<Double-1>', onObjectClick)    # теги тоже можно исп
canv.pack()
root.mainloop()
