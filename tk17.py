# Radiobutton радиокнопки
'создает группу переключателей, которые вызывают демонстрационные диалоги'


from tkinter import * # импортировать базовый набор виджетов
from tk6 import demos # импортировать готовые диалоги
from quitter import Quitter # прикрепить к 'себе' объект Quitter

class Demo(Frame):
    def __init__(self, parent=None, **options):
        Frame.__init__(self, parent, **options)
        self.pack()
        Label(self, text='Radio demos').pack(side=TOP)
        self.var = StringVar()
        for key in demos:
            Radiobutton(self, text=key,
                        command=self.onPress,
                        variable=self.var,
                        value=key).pack(anchor=NW)
        self.var.set(key) # при запуске выбрать последний переключатель
        Button(self, text='State', command=self.report).pack(fill=X)
        Quitter(self).pack(fill=X)
        
    def onPress(self):
        pick = self.var.get()
        print('you pressed', pick)
        print('result:', demos[pick]())

    def report(self):
        print(self.var.get())


if __name__ == '__main__': Demo().mainloop()