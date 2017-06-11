#!/usr/bin/python
# -*- coding: utf-8 -*-

# импортирование модулей python
from tkinter import *

# класс главного окна
class main:
  def __init__(self, master):
    self.master = master
    self.master.title('parent')
    self.master.geometry('200x150+300+225')
    self.button = Button(self.master,
                         text = 'myButton',
                         command = self.openDialog)
    self.button.pack(side = BOTTOM)
    self.master.mainloop()

  def openDialog(self):
    child(self.master)

# класс дочерних окон
class child:
  def __init__(self, master):
    self.slave = Toplevel(master)
    self.slave.title('child')
    self.slave.geometry('200x150+500+375')
    self.slave.grab_set()
    self.slave.focus_set()
    self.slave.wait_window()

# создание окна
root = Tk()

# запуск окна
main(root)
