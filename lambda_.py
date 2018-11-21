"""lambda - выражение, которое возвращает функцию. (Анонимная ф-ия)
используется: для передачи аргументов в функцию обработчика(command)
при создании: регестрируется и откладыват вызов фактической функции с
необходимымми параметрами"""

import sys
from tkinter import *


root = Tk()
win1 = Toplevel()

A = 100
B = 200


# вспомогательные ф-ии ====================
def handler(a, b):
    print("{} + {} = {}".format(a,b,a+b))

def func():
    handler(22, 33)

def glob_func():
    global A
    print('используем глобальные переменные А + В', A+B)
    A += 1

def loc_func():     # аргументы по умолчанию lnbda x=x: func(x) нужны для того чтобы запомнить x
    x = 666
    Button(win1, text='видимость в лок зоне, запоминает переменную {}'.format(x),
           command=lambda x=x: handler(x, 111)).pack()  # x=x для того чтобы х запомнилось в этот момент
    x -= 333    # тестируем, изменится ли тут - где x был равен 666 lambda: handler(x, 111) - да изменился 333
                # поэтому нужно делать аргументы по умолчанию lambda x=x: handler(x, 111) - так сохранится 666

def odd():
    funcs = []
    for c in 'abcdefg':
        funcs.append((lambda: c))   # поиск переменной c будет выполнен позднее
    return funcs                    # не сохраняет текущее значение c
for func in odd():
    print(func(), end=' ')          # Опа!: выведет 7 символов g, а не a,b,c,... !
print('\n')

def odd2():
    funcs = []
    for c in 'abcdefg':
        funcs.append((lambda c=c: c))   # запомнить текущее значение c
    return funcs                        # значения по умолчанию вычисляются немедленно

for func in odd2():
    print(func(), end=' ')              # OK: теперь выведет a,b,c,...
print('\n')
# =========================================


Label(root, text='root').pack()
btn1 = Button(root, text='lambda: print()', command=lambda: print('Отложенный вызов с пом lambda'))
btn2 = Button(root, text='print()', command=print('Эта надпись появится сразу и только 1 раз'))
btn3 = Button(win1, text="lambda: handler(A, B)", command=lambda: handler(A, B))
btn4 = Button(win1, text="func()->handler(A, B)", command=func)
btn5 = Button(win1, text="glob_func()", command=glob_func)  # не рекомендуется



btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()
btn5.pack()
loc_func()  # кнопка с локальной перем внутри ф-ии

mainloop()

