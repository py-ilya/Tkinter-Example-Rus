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
    self.text = Text(self.master,
                     background = 'white')
    self.text.pack(side = TOP,
                   fill = BOTH,
                   expand = YES)
    self.master.mainloop()

  def openDialog(self):
    child(self.master, self.text.get('0.0', END))

# класс дочерних окон
class child:
  def __init__(self, master, myText = ''):
    self.slave = Toplevel(master)
    self.slave.title('child')
    self.slave.geometry('200x150+500+375')
    self.text = Text(self.slave,
                     background = 'white')
    self.text.pack(side = TOP,
                   fill = BOTH,
                   expand = YES)
    self.text.insert('0.0', myText)
    self.slave.grab_set()
    self.slave.focus_set()
    self.slave.wait_window()

# создание окна
root = Tk()

# запуск окна
main(root) 
