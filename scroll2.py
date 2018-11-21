from tkinter import *

window = Frame()
vscroll = Scrollbar(window)
hscroll = Scrollbar(window, orient='horizontal')
listbox = Listbox(window)
# прокрутить список при перемещении движка в полосе прокрутки
vscroll.config(command=listbox.yview, relief=SUNKEN)
hscroll.config(command=listbox.xview, relief=SUNKEN)
# переместить движок в полосе прокрутки при прокрутке списка
listbox.config(yscrollcommand=vscroll.set, relief=SUNKEN)
listbox.config(xscrollcommand=hscroll.set)

window.mainloop()