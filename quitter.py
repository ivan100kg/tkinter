"создает панель с кнопками, которые вызывают диалоги"


from tkinter import * # импортировать базовый набор виджетов
from tkinter.filedialog import askopenfilename  # импортировать стандартные
from tkinter.colorchooser import askcolor       # диалоги из Lib\tkinter
from tkinter.messagebox import askquestion, showerror   #
from tkinter.simpledialog import askfloat
from tkinter.messagebox import askokcancel # импортировать стандартный диалог


# выход с подтверждением
class Quitter(Frame): # подкласс графич. интерфейса
    def __init__(self, parent=None): # метод конструктора
        Frame.__init__(self, parent)
        self.pack()
        widget = Button(self, text='Quit', command=self.quit)
        widget.pack(side=LEFT, expand=YES, fill=BOTH)

    def quit(self):
        ans = askokcancel('Verify exit', 'Really quit?')    # выход
        if ans: Frame.quit(self)


demos = {
    'Open': askopenfilename,    # выбрать файл в проводнике, возвращает полный путь к файлу
    'Color': askcolor,          # выбор цвета
    'Query': lambda: askquestion('Warning', 'You typed "rm *"\nConfirm?'),  # вопрос да нет, возвращает строки "yes" 'no'
    'Error': lambda: showerror('Error!', "He's dead, Jim"),         # ошибка
    'Input': lambda: askfloat('Entry', 'Enter credit card number')  # поле ввода, возвращает float, askinteger и askstring то же самое но int и str
}



class Demo(Frame):
    def __init__(self, parent=None, **options):
        Frame.__init__(self, parent, **options)
        self.pack()
        Label(self, text="Basic demos").pack()
        for (key, value) in demos.items():  # размещаем кнопки
            Button(self, text=key, command=value).pack(side=TOP, fill=BOTH)
        Quitter(self).pack(side=TOP, fill=BOTH)


if __name__ == '__main__': Demo().mainloop()
