#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    s1 = input("Введите первую строку: ")
    s2 = input("Введите вторую строку: ")

    set1 = set(s1)
    set2 = set(s2)

    common = set1.intersection(set2)

    if common:
        print(f"Общие символы: {''.join(common)}")
    else:
        print("Общих символов нет.")