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
                         text = 'dialog',
                         command = self.openDialog)
    self.button.pack(side = BOTTOM)
    self.text = Text(self.master,
                     background = 'white')
    self.text.pack(side = TOP,
                   fill = BOTH,
                   expand = YES)
    self.master.mainloop()

  def openDialog(self):
    self.dialog = child(self.master)
    self.sendValue = self.text.get('0.0', END)
    self.returnValue = self.dialog.go(self.sendValue)
    if self.returnValue:
      self.text.delete('0.0', END)
      self.text.insert('0.0', self.returnValue)

# класс дочернего окна
class child:
  def __init__(self, master):
    self.slave = Toplevel(master)
    self.slave.title('child')
    self.slave.geometry('200x150+500+375')
    self.button = Button(self.slave,
                         text = 'accept',
                         command = self.accept)
    self.button.pack(side = BOTTOM)
    self.text = Text(self.slave,
                     background = 'white')
    self.text.pack(side = TOP,
                   fill = BOTH,
                   expand = YES)

  def go(self, myText = ''):
    self.text.insert('0.0', myText)
    self.newValue = None
    self.slave.grab_set()
    self.slave.focus_set()
    self.slave.wait_window()
    return self.newValue

  def accept(self):
    self.newValue = self.text.get('0.0', END)
    self.slave.destroy()

# создание окна
root = Tk()

# запуск окна
main(root)
