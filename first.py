# coding=utf-8
"""
Написать функцию определения четности числа

def isEven(value):
    return value % 2 == 0
"""


def is_even(value):
    """
    Побитовый сдвиг дает целочисленное деление на 2.
    Если после побитового сдвига вправо применить побитовый сдвиг влево и значение останется прежним,
    значит исходное число было четным, иначе нечетным.

    Плюс - работа с битовыми представлениями чисел
    Минус - плохая читаемость кода

    :param value:
    :return: bool
    """
    return value >> 1 << 1 == value


if __name__ == '__main__':
    print is_even(6)
    print is_even(1241151)
