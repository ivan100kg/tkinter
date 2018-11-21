# балуемся с pack()

from tkinter import *


root = Tk()

Label(text='label1').pack(side=TOP)
Label(text='label2').pack(side=LEFT)
Label(text='label3').pack(side=LEFT)
Label(text='label4').pack(side=LEFT)
Label(text='label5').pack(side=TOP)
Label(text='label6').pack(side=TOP)
Label(text='label7').pack(side=TOP)
Label(text='label8').pack(side=LEFT)
Label(text='label9').pack(side=LEFT)
Label(text='label0').pack(side=LEFT)

if __name__ == '__main__':
    mainloop()