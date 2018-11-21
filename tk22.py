# Canvas PhotoImage пример

from tkinter import *


gifaddr = "C:/Users/Ivar/Pictures/Скрины/"

win = Tk()

img = PhotoImage(file=gifaddr + 's1200.gif')

can = Canvas(win)
can.pack(fill=BOTH)
can.config(width=img.width(), height=img.height())  # размер соотв картинке
can.create_image(2, 2,image=img, anchor=NW)  # координаты x y


mainloop()