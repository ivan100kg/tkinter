'''отображает изображение с помощью стандартного объекта PhotoImage из библиотеки
tkinter; данная реализация может работать с GIF-файлами, но не может
обрабатывать изображения в формате JPEG; использует файл с изображением, имя
которого указано в командной строке, или файл по умолчанию; используйте Canvas
вместо Label, чтобы обеспечить возможность прокрутки, и т.д.'''


import os, sys
from tkinter import *   # использовать стандартный объект PhotoImage
                        # работает с форматом GIF, а для работы с форматом JPEG
                        # требуется пакет PIL

from PIL.ImageTk import PhotoImage  # <== использовать альтернативный класс из
                                    # PIL, остальной программный код
                                    # без изменений

root = Tk()

imgpath = "C:/Users/Ivar/Pictures/Скрины/index.jpg"
root.title('...'+ imgpath[-10:])

imgobj = PhotoImage(file=imgpath)

Label(root, image=imgobj).pack(side=LEFT)

can = Canvas(root)
can.pack(side=LEFT)
can.create_image(0, 0, image=imgobj, anchor=NW)
can.config(width=imgobj.width(), height=imgobj.height())
print(imgobj.width(), imgobj.height())

root.mainloop()
