'''9. Написать функцию для перевода десятичного числа в другую систему исчисления (2-36).
Небольшая подсказка. В этой задаче вам понадобится:
    - список
    - метод `revers()` (или срез [::-1], или вместо `revers()` использовать `insert()` тогда не придётся разворачивать
    список), чтоб развернуть список, метод `join()`
    - строка `ascii_uppercase` из модуля `string` (её можно получить если сделать импорт `from string import
    ascii_uppercase`), она содержит все буквы латинского алфавита.'''
from string import ascii_uppercase


def new_system(lst, key_value, left=0, right=None):
    if right is None:
        right = len(lst)

    middle = (left + right) // 2
    while lst[middle] != key_value and left <= right:
        if lst[middle] < key_value:
            left = middle + 1
        else:
            right = middle - 1

        middle = (left + right) // 2

    return (True, middle) if not left > right else (False, middle+1)


l = [9, 29.5, 34, 36, 40, 50, 51, 53, 57, 78, 85, 88, 88, 89, 92, 94, 94, 95, 99, 100]
print(new_system(l, 54, 0))
print(new_system(l, 88, 0))
