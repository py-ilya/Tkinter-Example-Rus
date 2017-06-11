#!/usr/bin/python
# -*- coding: utf-8 -*-

# импортирование модулей python
from tkinter import *

# класс дочернего окна
class dialog:
  def __init__(self, master):
    self.top = Toplevel(master)
    self.top.title('dialog')
    self.top.geometry('200x100+300+250')
    self.frame = Frame(self.top)
    self.frame.pack(side = BOTTOM)
    self.accept_button = Button(self.frame,
                                text = 'accept',
                                command = self.accept)
    self.accept_button.pack(side = LEFT)
    self.cancel_button = Button(self.frame,
                                text = 'cancel',
                                command = self.cancel)
    self.cancel_button.pack(side = RIGHT)
    self.text = Text(self.top,
                     background = 'white')
    self.text.pack(side = TOP,
                   fill = BOTH,
                   expand = YES)
    self.top.protocol('WM_DELETE_WINDOW', self.cancel)

  def go(self, myText = '',):
    self.text.insert('0.0', myText)
    self.newValue = None
    self.top.grab_set()
    self.top.focus_set()
    self.top.wait_window()
    return self.newValue

  def accept(self):
    self.newValue = self.text.get('0.0', END)
    self.top.destroy()

  def cancel(self):
    self.top.destroy()

# тестовая команда
if __name__ == '__main__':
  root = Tk()
  root.withdraw()
  myTest = dialog(root)
  print (myTest.go('Hello World!'))
