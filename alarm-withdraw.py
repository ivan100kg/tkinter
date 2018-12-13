# то же самое, но скрывает и отображает окно целиком
from tkinter import *
import alarm
class Alarm(alarm.Alarm):
    def repeater(self):
        self.bell()
        if self.master.state() == 'normal':
            self.master.withdraw()
        else:
            self.master.deiconify()
            self.master.lift()
        self.after(self.msecs, self.repeater)
#
#
#
#
#
#
#
#
# каждые N миллисекунд
# подать сигнал
# окно отображается?
# скрыть окно, без ярлыка
# iconify свертывает в ярлык
# иначе перерисовать окно
# и поднять над остальными
# переустановить обработчик
if __name__ == '__main__': Alarm().mainloop() # master = корневое окно Tk
# по умолч
