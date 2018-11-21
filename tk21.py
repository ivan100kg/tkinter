# изображения PhotoImage() поддерживает gif ppm pgm

from tkinter import *


gifaddr = "F:/Programming/t1.gif"

win = Tk()

img = PhotoImage(file=gifaddr)

Button(win, image=img, command=win.quit).pack()


mainloop()
