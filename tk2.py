"""Frame"""

from tkinter import *


def greeting():
    print("Hello stdout world!...")


"""Frame - контейнер для других виджетов, каркас, рамка..."""
win = Frame()
win.pack(side=TOP, expand=YES, fill=BOTH)   # для увеличения каркаса со всеми его виджетами

# метка и две кнопки
Label(win,  text="Hello container world!").pack(side=TOP, expand=YES, fill=BOTH)
Button(win, text="Hello", command=greeting).pack(side=LEFT, expand=YES, fill=X)
Button(win, text="Quit",  command=win.quit).pack(side=RIGHT)


win.mainloop()