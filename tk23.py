# Pillow PIL переделывает форматы изображения, можно использовать любые форматы

from tkinter import *
from PIL.ImageTk import PhotoImage # <== добавьте эту строку, заменяет ф-ю из tkinter

root = Tk()

jpgaddr = "C:/Users/Ivar/Pictures/Скрины/index.jpg"
phoimj = PhotoImage(file=jpgaddr)

Button(image=phoimj).pack()

mainloop()
