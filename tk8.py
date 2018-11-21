"""то же, что и предыдущий пример, но выводит значения, возвращаемые диалогами;
lambda-выражение сохраняет данные из локальной области видимости для передачи их
обработчику (обработчик события нажатия кнопки обычно не получает аргументов,
а автоматические ссылки в объемлющую область видимости некорректно работают
с переменными цикла) и действует подобно вложенной инструкции def, такой как:
def func(key=key): self.printit(key)"""

from tkinter import *           # импортировать базовый набор виджетов
from tk6 import demos           # обработчики событий от кнопок
from quitter import Quitter     # прикрепить к себе объект quit


class Demo(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)    # create frame
        self.pack()                     # pack
        Label(self, text="Basic demos").pack()  # create label

        for key in demos:   # перебираем словарь
            Button(self, text=key, command=lambda key=key: self.printit(key)).pack(side=TOP, fill=BOTH)  # create button
            # command запоминает lambda с аргум. по умолчанию, т.к key потом изменится, в итоге получается при
            # нажатии на кнопку с именем, printit вызывает ф-ии в нутри словаря demos с ключами == имени кнопки
            # то что возвраается функциями выводится d stdout

        Quitter(self).pack(side=TOP, fill=BOTH) # create my button from file

    def printit(self, name):
        #     ключ                вызов ф-ии из словаря demos
        print(name, "returns =>", demos[name]())    #

if __name__ == '__main__':
    Demo().mainloop()
