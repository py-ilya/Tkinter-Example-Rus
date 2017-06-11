#!/usr/bin/python
# -*- coding: utf-8 -*-

# импортирование модулей python
from tkinter import *

#создание окна
root = Tk()
root.title('parent')
root.geometry('200x150+200+150')

#создание дочернего окна
child = Toplevel(root)
child.title('child')
child.geometry('200x150+400+300')

# запуск окна
root.mainloop()
