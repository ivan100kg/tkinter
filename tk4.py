# окна верхнего уровня Toplevel, protocol(), destroy(), quit(), title(), iconbitmap()

from tkinter import *


root = Tk()     # корневое окно


"""Toplevel - самостоятельное окно, компоновать не нужно"""
# два независимых окна являющиеся частью одного процесса
win1 = Toplevel(root)
win2 = Toplevel(root)


"""protocol() перехватывает события окна"""
win2.protocol('WM_DELETE_WINDOW', lambda:None)  # игнорировать закрытие ()


"""title() iconbitmap()"""
win2.title('второе окно')   # Заголовок окна
win2.iconbitmap("1.ico")    # Иконка, фотка с компа .ico


"""destroy() закрывает одно окно, если были окна-дети - тоже все закрываются"""
Button(win1, text='win1', command=win1.destroy).pack()  # destroy() закрывает одно окно


"""quit() закрывает главный цикл и программу, может применяться с любым виджетом"""
Button(win2, text='win2', command=win2.quit, width=80).pack()   # quit() закрывает программу


Label(root, text='Всплывающие окна - Popups').pack()   # в корневое окно

root.mainloop()