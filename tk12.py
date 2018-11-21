# Message - виджет отображения текста - подмножество виджета Text

from tkinter import *

msg = Message(text="Oh by the way, which one's Pink?")
msg.config(bg='pink', font=('consolas', 20, 'italic'))
msg.pack(fill=X, expand=YES)

mainloop()