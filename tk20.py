# ползунки и переменные
# моя допилка

from tkinter import *

root = Tk()

x = IntVar()
y = IntVar()

def report():
    #print(sclv.get())
    y.set(x.get())
    print(x.get())
    print(y.get())

def reset():
    y.set(0)
    x.set(0)

sclv = Scale(root,
             label='vertical',      # метка ползунка
             orient='vertical',     # направленность
             from_=180, to=-180,    # шкала от и до
             tickinterval=90,       # цена деления шкалы
             resolution=1,          # шаг перемещения ползунка
             variable=x,            # связанные переменные
             showvalue=YES          # отображение значения позунка
             # command=report       # связанный метод
             )

sclh = Scale(root,
             label='horizontal',    # метка ползунка
             orient='horizontal',   # направленность
             from_=-180, to=180,    # шкала от и до
             tickinterval=90,       # цена деления шкалы
             resolution=1,          # шаг перемещения ползунка
             variable=y,            # связанные переменные
             showvalue=YES          # отображение значения позунка
             # command=report       # связанный метод)
             )

sclv.pack(expand=YES, fill=Y)
sclh.pack(expand=YES, fill=X)






Button(root, text='сравнять', command=report).pack(side=RIGHT)
Button(root, text='reset', command=reset).pack(side=LEFT)
root.mainloop()
