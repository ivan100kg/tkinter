from tkinter import *


def click(event):
    print('got key press', event.char)
    for key in event.__dict__:
        print(key, '=>', event.__dict__[key])


lbl = Label(text="#"*80)
lbl.config(bg='blue', height=16, width=80)
lbl.pack()
lbl.bind('<KeyPress>', click)
lbl.focus() # фокус на виджет
btn = Button(text='привет')
btn.pack(fill=X)



mainloop()
