#!/usr/bin/python
# -*- coding: utf-8 -*-

# импортирование модулей python
from tkinter import *

# класс главного окна
class main:
  def __init__(self, master):
    self.master = master
    self.master.title('myWindow')
    self.master.geometry('200x150+300+225')
    self.button = Button(self.master,
                         text = 'myButton')
    self.button.pack(side = BOTTOM)
    self.master.mainloop()

# создание окна
root = Tk()

# запуск окна
main(root)
