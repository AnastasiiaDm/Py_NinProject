'''9. Написать функцию для перевода десятичного числа в другую систему исчисления (2-36).
Небольшая подсказка. В этой задаче вам понадобится:
    - список
    - метод `revers()` (или срез [::-1], или вместо `revers()` использовать `insert()` тогда не придётся разворачивать
    список), чтоб развернуть список, метод `join()`
    - строка `ascii_uppercase` из модуля `string` (её можно получить если сделать импорт `from string import
    ascii_uppercase`), она содержит все буквы латинского алфавита.'''


def new_system():
    num = int(input())
    base = int(input("Base (2-36): "))
    if not (2 <= base <= 36):
        quit()

    newNum = ''

    while num > 0:
        newNum = str(num % base) + newNum
        num //= base

    print(newNum)


new_system()
