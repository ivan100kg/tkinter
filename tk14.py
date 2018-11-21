# Entry, StringVar() - после уничтожения окна, продолжает жить

"""непосредственное использование виджетов Entry и размещение их по рядам с метками
фиксированной ширины: такой способ компоновки, а также использование менеджера
grid обеспечивают наилучшее представление для форм"""


from tkinter import *
from quitter import Quitter


fields = 'Name', 'Job', 'Pay'


def fetch(entries):
    for entry in entries:
        print('Input => “%s”' % entry.get()) # извлечь текст
        print(var.get())  # выводит значение


def makeform(root, fields, var):
    entries = []

    for field in fields:
        row = Frame(root) # создать новый ряд
        lab = Label(row, width=5, text=field) # добавить метку, поле ввода
        ent = Entry(row)
        row.pack(side=TOP, fill=X) # прикрепить к верхнему краю
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X) # растянуть по горизонтали
        entries.append(ent)

    entries[0].config(textvariable=var) # прикрепим к первому Entry нашу StrirngVar
    entries[0].focus()  # фокус на 1-ом поле ввода
    var.set('Введи что-ниб')    # еще один способ заполнить поле

    return entries
    
    
if __name__ == '__main__':
    root = Tk()
    var = StringVar()  # объект стринг в ткинтер см. дальше
    ents = makeform(root, fields, var)
    root.bind('<Return>', (lambda event: fetch(ents)))
    Button(root, text='Fetch', command = (lambda: fetch(ents))).pack(side=LEFT)
    Quitter(root).pack(side=RIGHT)
    root.mainloop()