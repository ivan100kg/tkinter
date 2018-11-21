from tkinter import *
from tkinter.simpledialog import askfloat
from tkinter.filedialog import askopenfilename  # импортировать стандартные

root = Tk()
f = askfloat('hui', 'size hui')
a = askopenfilename()

root.mainloop()
print(f)
print(a)