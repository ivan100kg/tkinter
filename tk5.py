# диалоги


from tkinter import *
from tkinter.messagebox import *


# стандртные диалоги, блокируют программу до нажатия подтверждения
""" askyesno()    - ? выбор - 2 кнопки Да Нет возвращает True False
    showwarning() - ! предупреждение - 1 кнопка OK
    showinfo()    - информация - 1 копка OK
    showerror()   - X ошибка - 1 кнопка OK
    askokcancel() - ? вопрос - 2 кнопки OK Cancel возвращает True False"""


def callback():
    if askyesno("Verify", "Do you really want to quit?"):
        showwarning("Yes", "Quit not yet implemented")
    else:
        showinfo("No", "Quit has been cancelled")

def naher():
    if askokcancel("Выход?", "Выйти нахер?"):
        quit()
    else:
        pass


errmsg = "Sorry, no Spam allowed!"
Button(text='Quit', command=callback).pack(fill=X)
Button(text="Spam", command=(lambda: showerror("Spam", errmsg))).pack(fill=X)
Button(text='Выход', command=naher).pack(fill=X)




mainloop()
