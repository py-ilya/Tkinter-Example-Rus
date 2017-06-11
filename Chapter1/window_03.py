#!/usr/bin/python
# -*- coding: utf-8 -*-

# импортирование модулей python
from tkinter import *

# класс родительских окон
class main:
  def __init__(self):
    self.master = root
    self.master.title('parent')
    self.master.geometry('200x150+200+150')
    child()
    self.master.mainloop()

# класс дочерних окон
class child:
  def __init__(self):
    self.slave = Toplevel(root)
    self.slave.title('child')
    self.slave.geometry('200x150+400+300')

# создание окна 
root = Tk() 

# запуск окна 
main()
