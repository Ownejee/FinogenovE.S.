# -*- coding: utf-8 -*-

def count():
    a = input("Введите слова: ")
    print("Ответ: ")
    return a.count(" ") + 1

print(count())