# -*- coding: utf-8 -*-

from tkinter import *

def stringOperations():
    arg = txt1.get()
    n = int(arg)
    i=1
    result = []
    while i ** 2 <= n:
        result.append(str(i**2))
        i += 1
    resultlbl_2.configure(text = ",".join(result))

def count():
    arg = txt2.get()
    n = int(arg)
    i=2
    while n % i != 0:
        i += 1
    resultlbl1_2.configure(text = i)

window = Tk()
window.title("Решение 6го занятия")
lbl = Label(window, text = "Введите число:")
lbl.grid(column=0, row = 0)
txt1 = Entry(window, width = 10)
txt1.grid(column=1, row = 0)
btn = Button(window, text = "Выполнить фукнцию 1", command = stringOperations )
btn.grid(column=2, row = 0)
resultlbl_1 = Label(window, text = "Результат: ")
resultlbl_1.grid(column = 3, row = 0)
resultlbl_2 = Label(window, text = "")
resultlbl_2.grid(column=4, row = 0)

lbl1 = Label(window, text = "Введите число больше 2:")
lbl1.grid(column=0, row = 1)
txt2 = Entry(window, width = 10)
txt2.grid(column=1, row = 1)
btn1 = Button(window, text = "Выполнить функцию 2",command = count)
btn1.grid(column=2, row = 1)
resultlbl1_1 = Label(window, text = "Результат: ")
resultlbl1_1.grid(column = 3, row = 1)
resultlbl1_2 = Label(window, text = "")
resultlbl1_2.grid(column=4, row = 1)

window.mainloop()