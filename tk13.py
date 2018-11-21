# Entry - виджет служит простым полем ввода одной строки текста

from tkinter import *
from quitter import Quitter


def fetch():
    # ent.get() - строка которую ввели
    print('Input => “%s”' % ent.get()) # извлечь текст


root = Tk()
ent = Entry(root)

ent.insert(0, 'Type words here') # записать текст
ent.pack(side=TOP, fill=X) # растянуть по горизонтали
ent.focus() # избавить от необходимости выполнять щелчок мышью

ent.bind('<Return>', (lambda event: fetch())) # по нажатию клавиши Enter
btn = Button(root, text='Fetch', command=fetch) # и по щелчку на кнопке
btn.pack(side=LEFT)

Quitter(root).pack(side=RIGHT)
root.mainloop()