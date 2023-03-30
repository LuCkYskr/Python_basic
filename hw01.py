"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(lst):
    return [i**2 for i in lst]

    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def fun_siml(value):
    flag = True
    if value <= 2:
        flag = False
        return flag
    if value > 2:
        for i in range(2, value):
            if value % i == 0:
                flag = False
                break

    return flag

def filter_numbers(lst, const):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)
    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if const == "odd":
        return [i for i in lst if i % 2 == 0]
    if const == "even":
        return [i for i in lst if i % 2 != 0]
    if const == "prime":
        return [i for i in lst if fun_siml(i)]


lst =  [1, 2, 5, 7, 9, 12, 11]
print(power_numbers(lst))
print(fun_siml(1))
print(filter_numbers(lst, ODD))
print(filter_numbers(lst, EVEN))
print(filter_numbers(lst, PRIME))