#!/usr/bin/python
# -*- coding: utf-8 -*-

# импортирование модулей python
from tkinter import *
from myBoolean import *
from myDialog import *

# класс главного окна
class main:
  def __init__(self, master):
    self.master = master
    self.master.title('main')
    self.master.geometry('400x300+200+150')
    self.button = Button(self.master,
                         text = 'dialog',
                         command = self.openDialog)
    self.button.pack(side = BOTTOM)
    self.text = Text(self.master,
                      background = 'white')
    self.text.pack(side = TOP,
                   fill = BOTH,
                   expand = YES)
    self.master.protocol('WM_DELETE_WINDOW',
                         self.exitMethod)
    self.master.mainloop()

  def openDialog(self):
    self.dialog = dialog(self.master)
    self.sendValue = self.text.get('0.0', END)
    self.returnValue = self.dialog.go(self.sendValue)
    if self.returnValue:
      self.text.delete('0.0', END)
      self.text.insert('0.0', self.returnValue)

  def exitMethod(self):
    self.dialog = yesno(self.master)
    self.myMssg = 'Do you want to exit?'
    self.returnValue = self.dialog.go(message = self.myMssg)
    if self.returnValue:
      self.master.destroy()

# создание окна
root = Tk()

# запуск окна
main(root)
