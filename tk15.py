# модальный диалог с формой, данные извлекаются до уничтожения окна
# Если нажать кнопку в главном окне, сценарий создаст окно диало-
# га с формой, блокирующее остальное приложение


from tkinter import *
from tk14 import makeform, fetch, fields


def show(entries, popup):
    fetch(entries) # извлечь данные перед уничтожением окна!
    popup.destroy() # если инструкции поменять местами, сценарий будет возбуждать исключение


def ask():
    popup = Toplevel() # отобразить форму в виде модального диалога
    ents = makeform(popup, fields)
    Button(popup, text='OK', command=(lambda: show(ents, popup))).pack()
    popup.grab_set()
    popup.focus_set()
    popup.wait_window() # ждать закрытия окна


root = Tk()
Button(root, text='Dialog', command=ask).pack()
root.mainloop()
