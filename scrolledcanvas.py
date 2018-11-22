# простой компонент холста с вертикальной прокруткой

from tkinter import *

class ScrolledCanvas(Frame):
    def __init__(self, parent=None, color='brown'):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)
        canv = Canvas(self, bg=color, relief=SUNKEN)
        canv.config(width=300, height=200)
        canv.config(scrollregion=(0, 0, 1000, 10000))
        canv.config(highlightthickness=0)
        sbar = Scrollbar(self)
        sbar_x = Scrollbar(self)
        sbar.config(command=canv.yview)
        sbar_x.config(command=canv.xview, orient='horizontal')
        # связать sbar и canv
        canv.config(yscrollcommand=sbar.set) # сдвиг одного = сдвиг другого
        sbar.pack(side=RIGHT, fill=Y)
        canv.config(xscrollcommand=sbar_x.set) # сдвиг одного = сдвиг другого
        sbar_x.pack(side=BOTTOM, fill=X)
        # первым добавлен – посл. обрезан
        canv.pack(side=LEFT, expand=YES, fill=BOTH) # canv обрезается первым
        self.fillContent(canv)
        canv.bind('<Double-1>', self.onDoubleClick) # установить обр. события
        self.canvas = canv
    def fillContent(self, canv):
        for i in range(100):
            canv.create_text(150, 50+(i*100), text='spam'+str(i),fill='beige')
    def onDoubleClick(self, event):
        print(event.x, event.y)
        print(self.canvas.canvasx(event.x), self.canvas.canvasy(event.y))
if __name__ == '__main__': ScrolledCanvas().mainloop()
