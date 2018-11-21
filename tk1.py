"""Label, Button, pack(), bind(), quit(), config()"""

from tkinter import *
import sys


root = Tk()     # корневое окно(главное)


def print_text(text):
    print(text)

def dubble_def():
    print_text('двойной вызов def более неудобно def() -> def()')

def hello(event):
    print('одиночный щелчок, нажмите двойным')

def quit(event):
    print("Двойной клик ==> выхожу")
    sys.exit()

class Hello:
    def __init__(self):
        self.x = 42
        self.y = 'hui'
        self.knopka = Button(text='class method', command=self.print_xy)

    def print_xy(self):
        print(self.x,self.y, 'методы класса отлично подходят под замену глоб переменных и lambda')


hel = Hello()


#===============================================================================
"""Label - метка"""
metka = Label(root, text='Hello GUI world!')   # создать виджет
#              род. окно|текст метки
metka['text'] = 'Another my text'      # установка текста метки с пом. ключа словаря
metka.config(text='And final text!')   # установка текста с помощью метода config/configure
metka.configure(text='And really final text :)') # configure = config

# шрифт
labelfont = ('times', 20, 'bold')       # семейство, размер, стиль(normal, bold, roman, italic, underline, overstrike)
# config() - различные параметры виджета
metka.config(bg='black', fg='yellow')   # черный фон, желтый текст или 16-ричный "#66CDAA"
metka.config(font=labelfont)            # наш шрифт
metka.config(height=5, width=20)        # начальный р-р: строк, символов
metka.config(bd=20, relief=SUNKEN)      # bd - бордюр, ширина границы. relief - стиль(FLAT, SUNKEN, RAISED, GROOVE, SOLID или RIDGE)
metka.config(cursor='gumby')            # внеш вид курсора watch, pencil, cross и hand2


"""Button - кнопка"""
knopka = Button(root, bg='red',  text='this is exit==>', command=sys.exit)
knopka2 = Button(root, text='this is exit too==>', command=root.quit)   # .quit закрывает все окна и mainloop
# lambda нужна когда есть передаваемые аргументы, чтобы сразу не вызвать а после нажатия кнопки
knopka3 = Button(root, text='lambda action', command=lambda : print('lambda : def("huinana")'))    # так правильно сразу не печатает, а как бы откладывает на потом, после нажатия кнопки
knopka4 = Button(root, text='двойной вызов def', command=dubble_def)    # ссылка на функцию - все ок
knopka5 = Button(root, text='Привет мир событий!', cursor='hand2')


"""pack - компоновщик"""
metka.pack(side=TOP,        expand=YES,      fill=BOTH,      anchor=CENTER,      padx=20, pady=40)       # разместить
#           к какому краю  |YES - выделять  |BOTH - по обеим|яккорь - в какой   |отступы по x и y
#           род. окна прил.|виджету все своб|X - по оси x   |части выделяемого  |
#           TOP BOTTOM     |прост-во не зан.|Y - по оси y   |места расположить  |
#           LEFT RIGHT     |друг. вид-ми    |               |виджет. N,S,W,E,NW,NE,SW,SE,CENTER(по умолч))


knopka.pack(side=LEFT)
knopka2.pack(side=LEFT)
knopka3.pack(side=LEFT)
knopka4.pack(side=LEFT)
hel.knopka.pack(side=LEFT)


"""bind - обработчик событий"""
knopka5.pack(side=LEFT)
knopka5.bind("<Button-1>", hello)   # привязать обработчик щелчка
knopka5.bind("<Double-1>", quit)    # привязать обработчик 2-го щелчка




root.mainloop()   # запустить цикл событий
