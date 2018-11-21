# Меню представляют собой раскрывающиеся списки, которые обычно
# можно увидеть в верхней части окна

# меню окна верхнего уровня в стиле Tk8.0


from tkinter import * # импортировать базовый набор виджетов
from tkinter.messagebox import * # импортировать стандартные диалоги


def notdone():
    showerror('Not implemented', 'Not yet available')
    
def makemenu(win):
    top = Menu(win) # прикрепить меню к окну
    win.config(menu=top) # связать окно и меню

    file = Menu(top)    # прикрепить меню к меню верх ур
    file.add_command(label='New...', command=notdone, underline=0)  # underline - горячая клавиша для пункта меню
    file.add_command(label='Open...', command=notdone, underline=0)
    file.add_command(label='Quit', command=win.quit, underline=0)
    top.add_cascade(label='File', menu=file, underline=0) # связать родителя с потомком

    edit = Menu(top, tearoff=False) # tearoff - пунктирная линия
    edit.add_command(label='Cut', command=notdone, underline=0)
    edit.add_command(label='Paste', command=notdone, underline=0)
    edit.add_separator()    # линия разделитель
    top.add_cascade(label='Edit', menu=edit, underline=0)

    submenu = Menu(edit, tearoff=True)
    submenu.add_command(label='Spam', command=win.quit, underline=0)
    submenu.add_command(label='Eggs', command=notdone, underline=0)
    edit.add_cascade(label='Stuff', menu=submenu, underline=0)

    mymenu1 = Menu(edit, tearoff=False)
    mymenu1.add_command(label='hui', underline=0)
    edit.add_cascade(label='mymenu1', menu=mymenu1, underline=0)

    mymenu2 = Menu(top, tearoff=True)
    mymenu2.add_command(label='hui2', underline=0)
    top.add_cascade(label='mymenu2', menu=mymenu2, underline=0)

if __name__ == '__main__':
    root = Tk() # или Toplevel()
    root.title('menu_win') # информация для менеджера окон
    makemenu(root) # создать строку меню
    msg = Label(root, text='Window menu basics') # добавить что-нибудь ниже
    msg.pack(expand=YES, fill=BOTH)
    msg.config(relief=SUNKEN, width=40, height=7, bg='beige')
    root.mainloop()