# -*- coding: utf-8 -*-

s = input("Введите строку: ")
print(s[(len(s) + 1) // 2:] + s[:(len(s) + 1) // 2])