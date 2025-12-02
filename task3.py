#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    school = {
        '1а': 25,
        '1б': 28,
        '2а': 30,
        '2б': 27,
        '3а': 29,
        '4а': 31,
        '5а': 30,
    }

    print("Исходное состояние школы:")
    for klass, count in school.items():
        print(f"{klass}: {count} учеников")

    school['2а'] = 32
    print("\nа) Количество учеников в классе '2а' изменено на 32.")

    school['6а'] = 26
    print("б) Добавлен новый класс '6а' с 26 учениками.")

    del school['1б']
    print("в) Класс '1б' расформирован.")

    total_students = sum(school.values())

    print(f"\nОбщее количество учащихся в школе: {total_students}")