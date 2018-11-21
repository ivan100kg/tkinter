# Text

"""простой компонент просмотра текста или содержимого файла"""

from tkinter import *


class ScrolledText(Frame):
    def __init__(self, parent=None, text="", file=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH) # сделать растягиваемым
        self.makewidgets()
        self.settext(text, file)

    def makewidgets(self):
        sbar = Scrollbar(self)
        text = Text(self, relief=SUNKEN, bg='green')
        sbar.config(command=text.yview)  # связать sbar и text
        text.config(yscrollcommand=sbar.set)  # сдвиг одного = сдвиг другого
        sbar.pack(side=RIGHT, fill=Y)  # первым добавлен - посл. обрезан
        text.pack(side=LEFT, expand=YES, fill=BOTH)  # Text обрезается первым
        self.text = text

    def settext(self, text='', file=None):
        if file:
            text = open(file, 'r').read()
        self.text.delete('1.0', END)  # удалить текущий текст
        self.text.insert('1.0', text)  # добавить в стр. 1, кол. 0 первая строка первая колонка
        self.text.mark_set(INSERT, END)  # установить курсор вставки в конец
        self.text.focus()  # сэкономить щелчок мышью

    def gettext(self):  # возвращает строку
        return self.text.get('1.0', END + '-1c')  # от начала до конца, -1c отрезает замыкающий символ \n


if __name__ == '__main__':
    root = Tk()
    if len(sys.argv) > 1:
        st = ScrolledText(file=sys.argv[1]) # имя файла в командной строке
    else:
        st = ScrolledText(text='Words\ngo here\n') # иначе: две строки
        
    def show(event):
        print(repr(st.gettext())) # вывести как простую строку

    root.bind('<Key-Escape>', show) # esc = выводит дамп текста
        
    root.mainloop()