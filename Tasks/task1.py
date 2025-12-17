#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    s = input("Введите строку: ")

    count = 0
    for char in s:
        if char in vowels:
            count += 1

    print(f"Количество гласных: {count}")