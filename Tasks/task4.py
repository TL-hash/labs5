#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    nums = {
         2: 'ab',
         4: 'cd',
         6: 'ef',
         8: 'gh',
        10: 'ij',
        12: 'kl',
        13: 'mo',
    }

    print(f"Исходный словарь: {nums}")

    dict_items = nums.items()

    swapped = {v: k for k, v in dict_items}

    print(f"\nСловарь, 'обратный' исходному: {swapped}")


